class PublisherNode : public rclcpp::Node{

    public: 

        PublisherNode(const NodeOptions& options) : Node("PublisherNode"), cap(0){

            //on definit le qos en best effort et volatile

            publisher_ = this->create_publisher<sensor_msgs::msg::Image>("topic_image", qos);
            timer_ = this->create_wall_timer(std::chrono::milliseconds(500),[this](){this->timerCallback();})


        }

    private:

            //def de publisher et timer
            cv::Videocapture cap;

        void timerCallback(){

            cv::Mat Image;
            cap >> Image;

            //conversion cv vers mesg ros;

            std_msgs::Header header;
            header.stamp = this->get_clock()->now();
            header.frame_id = "camera link";

            auto msg = std::make_unique<sensor_msgs::msg::Image>();

            cv_bridge::CvImage(header, "bgr8", msg).toImageMsg(*msg);

            publisher_ -> publish(std::move(msg));

        }
}

RCLCPP_COMPONENTS_REGISTER_NODE(PublisherNode);