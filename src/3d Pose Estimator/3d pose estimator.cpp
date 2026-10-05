class ArucoPoseEstimator : public rclcpp::Node {


    public : 

        ArucoPoseEstimator() : Node("ArucoPoseEstimator"){

            this->declare_parameter<double>("aruco_size", 0.1);
            this->declare_parameter<int>("aruco_dict", 1); // enum sur les aruco_dic

            aruco_size = this->get_parameter("aruco_size").as_double();
            int dict_id = this->get_parameter("aruco_dict").as_int();
            dictionary = getPredefinedDictionnary(dict_id);
            
            tf_publisher_ = std::make_shared<tf2_ros::TransformBroadcaster>()
            subscriber_ = this->create_subscription<sensor_msgs::msg::Image>("topic/image", 10, [this](const std::shared_ptr<sensor_msgs::msg::Image>& msg){this->callbackSubscriber(image);});

            //valeurs obtenues de la calibration matérielle camera dun code exterieur pour la caméra actuellement utilisée, est ce correct de faire ainsi ? déclaration en private puis initialisation dans le cosntructeur
            MatrixIntra = //def matrice intra

            MatrixDistortion = //def de la matrice de distrortion

        }

        void callbackSubscriber(const std::shared_ptr<sensor_msgs::msg::Image>& msg){

            cv::Mat image;
            cv_bridge::CvImageConstPtr ptr = cv_bridge::toCvShare(msg, "bgr8");
            image = ptr->image;

            std::vector<cv::Point3f> aruco_real_size{
                cv::Point3f(-aruco_size/2, aruco_size/2,0.0),
                cv::Point3f(aruco_size/2, aruco_size/2,0.0),
                cv::Point3f(aruco_size/2, -aruco_size/2,0.0),
                cv::Point3f(-aruco_size/2, -aruco_size/2,0.0);
            }

            cv::detectMarkers(image,dictionary,corners,ids);

            for (size_t i=0; i < corners.size(); i++){
                std::cout << ids[i]; <<std::endl; //num du tag
                std::cout << corners[i].[0].x << corners[i].[0].y <<std::endl; //coo haut gauche
                std::cout << ids[i]; <<std::endl; //coo haut droit 1 a la place du 0
                std::cout << ids[i]; <<std::endl; //coo bas droit 2 a la place du 0
                std::cout << ids[i]; <<std::endl; //coo bas gauche 3 a la place du 0

                cv::Mat rvec,tvec;

                cv::solvePnP(aruco_real_size,corners[i], MatrixIntra, MatrixDistortion, rvec, tvec)

                geometry_msgs::msg::TransformStamped tf;
                tf.header.stamp = this->get_clock()->now();
                tf.header.parent_frame_id = "camera_link";
                tf.header.child_frame_id = "aruco" + std::to_string(ids[i]);

                tf.transform.translation.x = tvec.at<double>(0,0);
                tf.transform.translation.y = tvec.at<double>(0,1);
                tf.transform.translation.z = tvec.at<double>(0,2);

                tf2::Quaternion quat;
                cv::Mat cv_mat;
                tf2::Matrix3x3 ros_mat;

                cv::rodrigues(rvec,cv_mat);

                ros_mat(
                    cv_mat.at<double>(0,0),cv_mat.at<double>(0,1),cv_mat.at<double>(0,2),
                    cv_mat.at<double>(1,0),cv_mat.at<double>(1,1),cv_mat.at<double>(1,2),
                    cv_mat.at<double>(2,0),cv_mat.at<double>(2,1),cv_mat.at<double>(2,2)
                )

                ros_mat.getRotation(quat);

                tf.transform.rotation.x = quat.x();
                tf.transform.rotation.y = quat.y();
                tf.transform.rotation.z = quat.z();
                tf.transform.rotation.w = quat.w();

                tf_publisher_ -> sendTransform(tf);
                }

            
        }


    private :

        std::shared_ptr<tf2_ros::TransformPublisher> tf_publisher_;
        std::vector<int> ids;
        std::vector<std::vector<cv::Point>> corners;
        cv::Ptr<cv::aruco::Dictionary> dictionary;
        double aruco_size;
        cv::Mat MatrixIntra;
        cv::Mat MatrixDistortion;
}

int main(int argc, char* argv[]){

    rclcpp::init(argc,argc);
    rclcpp::spin(std::make_shared<ArucoPoseEstimator>(););
    rclcpp::shutdown();

}