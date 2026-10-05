class KF{

    public:
        KF(){

           //initialisation de toutes les matrices apres les calculs, G= 0
        }


        void predict(){
            //ecriture des formules pour déterminer Xk+1, Pk+1

            X = F*X;
            P = F*P*F.transpose() + Q;

        }

        void update(double x, double y){

            Eigen::Matrix<double,2,1> mesure;
            mesure << x,y;
            K = P*H.transpose()*(H*P*H.transpose()+ R).inverse();
            X = X + K*(mesure - H*X);
            P = (I - K*H) * P;

            std::cout << "estimation posx posy vx vy respectivement" << X(0,0) << X(1,0) << X(2,0) << X(3,0); <<std::endl;
        }

    private:


        
        Eigen::Matrix<double,2,4> H;
        Eigen::Matrix<double,2,2> R;
        Eigen::Matrix4d I = Eigen::Matrix4d::Identity();
        Eigen::Matrix4d P = I*1e4;
        Eigen::Matrix<double,4,1> X;
        Eigen::Matrix<double,4,4> Q;
        Eigen::Matrix<double,4,2> K;
        Eigen::Matrix<double,4,4> F;

}

class StateEstimator : public rclcpp::Node{

    public:

        StateEstimator(const NodeOptions& options) : Node("StateEstimator", options){

            rclcpp::QoS qos(10);
            qos.reliability(rclcpp::ReliabilityPolicy::BestEffort);
            qos.durability(rclcpp::DurabilityPolicy::Volatile);


            subscriber_ = this->create_subscription<sensor_msgs::msg::Image>("topic",qos, [this](std::shared_ptr<const sensor_msgs::msg::Image> msg){this->callbackSubscriber(msg);});

        }

    private:
        
        //def subscriber
        KF my_kf;

        void callbackSubscriber(const std::shared_ptr<const sensor_msgs::msg::Image> msg) {

            cv::Mat Image;
            cv_bridge::CvImageConstPtr ptr = cv_bridge::toCvShare(msg, "bgr8");
            Image = ptr->image;

            cv::Mat hsv,mask;
            cv::cvtColor(Image,hsv,cv::COLOR_BGR2HSV);

            //on suppose quon tracke un objet rouge;
            cv::Scalar high(0,70,70);
            cv::Scalar low(10,255,255); 
            cv::inRange(hsv,low,high,mask);

            std::vector<std::vector<cv::Point>> contours;

            cv::findContours(mask,contours, cv::RETR_EXTERNAL, cv::CHAIN_APPROX_SIMPLE);

            double max_area = 0;
            double coordinate_x = 0;
            double coordinate_y = 0;

            for (const auto& contour : contours){

                cv::Moments M = cv::moments(contour);

                double area = M.m00;

                if (area > max_area){
                    max_area = area;
                    coordinate_x = M.m10/M.m00;
                    coordinate_y = M.m01/M.m00 ;
                }
                }
                myKF.predict();

                if (max_area > 0){
                    //on detecte une image valide alors on update;
                    myKF.update(coordinate_x, coordinate_y);
                }
        }
};

int main(int argc, char* argv[]){
    rclcpp::init(argc,argv);
    options.use_intra_process_comms(true);
    rclcpp::spin(std::make_shared<StateEstimator>(options));
    rclcpp::shutdown();
    return 0;

}