class PID{

    public:

        PID(double p, double i, double d) : kp(p), ki(i), kd(d){}


        double compute(double dt, double error){

            double proportional = kp*error;

            integration_sum += error*dt;
            //anti windup
            integration_sum = std::clamp(integration_sum, -max_integral, max_integral);
            double integral = integration_sum*ki;
    
            double derivative = kd*(error-last_error)/dt;

            last_error = error;

            return proportional + integral + derivative;


        }

    private:
        double kp =1;
        double ki = 0.1;
        double kd = 0.01;
        double integration_sum = 0;
        double last_error = 0;
        double max_integral = 10;



    
};


class ActionServer : public rclcpp::Node{

    public:

        ActionServer() : Node("ActionServer"){

            //on met le this pour donner l'accès au noeud au serveur (car rclcpp_action ne fait pas partie de la classe node)
            server_ = rclcpp_action::create_server<nom_package::action::nom_struct>(this, "nom_topic_action",
            [this](const rclcpp_action::GoalUUID& uuid, const std::shared_ptr<const nom_package::action::nom_struct::Goal>> goal){return this->handle_goal(uuid,goal);}
            [this](const std::shared_ptr<rclcpp_action:ServerGoalHandle<const nom_package::action::nom_struct>> goal_handle){return this->handle_cancel(goal_handle);}
            [this](const std::shared_ptr<rclcpp_action:ServerGoalHandle<const nom_package::action::nom_struct>> goal_handle){this->handle_accept(goal_handle);}

            tf_buffer = std::make_shared<tf2_ros::Buffer>(this->get_clock());
            tf_listener_ = std::make_shared<tf2_ros::TransformLister>(*buffer);
        );


        }

    private:

    //def du buffer, lsitener, server


        bool SeeObjectX(){
            bool see = buffer -> canTransform("camera_link","objectX_tf", tf2::PointTimeZero);
            return see;

        }


        rclcpp_action::GoalResponse handle_goal(const rclcpp_action::GoalUUID& uuid, const std::shared_ptr<const nom_package::action::nom_struct::Goal>> goal){
                bool vision = SeeObjectX();
                // if demande aberrante ou inacceptable en loccurance ici si l'objet n'est pas visible donc sa tf nest pas présente 
                if (!vision){
                    return rclcpp_action::GoalResponse::REJECT;
                }
                else{
                     return rclcpp_action::GoalResponse::ACCEPT_AND_EXECUTE;
                }

        }

        rclcpp_action::CancelResponse handle_cancel(const std::shared_ptr<rclcpp_action::ServerGoalHandle<const nom_package::action::nom_struct>> goal_handle){
            return rclcpp_action::CancelResponse::ACCEPT;
        }

        void handle_accept(const std::shared_ptr<rclcpp_action::ServerGoalHandle<const nom_package::action::nom_struct>> goal_handle){

            auto execute_thread = [this,goal_handle](){this->execute(goal_handle);};

            std::thread ThreadExecute(execute_thread);

            ThreadExecute.detach();
        }


        void execute(const std::shared_ptr<rclcpp_action::ServerGoalHandle<const nom_package::action::nom_struct>> goal_handle){

            const std::shared_ptr<const nom_package::action::nom_struct::Goal>> goal = goal_handle.get_goal();
            const std::shared_ptr<const nom_package::action::nom_struct::Feedback> feedback = std::make_shared<const nom_package::action::nom_struct::Feedback>();
            const std::shared_ptr<const nom_package::action::nom_struct::Result> result = std::make_shared<const nom_package::action::nom_struct::Feedback>();

            rclcpp::Rate loop(10);

            PID myPID(1,0.1,0.01);

            while (!goal_handle->is_canceling()){

                bool see = SeeObjectX();

                if (goal_handle->is_canceling()){
                    result->termine = false;
                    goal_handle->canceled(result);
                    return;
                }

                if (!see){
                    result->termine = false;
                    goal_handle->abort(result);
                    return;
                }

                geometry_msgs::msg:TransformStamped tf;

                tf = buffer_ -> lookupTransform("base_link", "objectX", tf2::TimePointZero);

                double error = tf.transform.translation.x; //différence de distance selon x entre le robot et lobjet x
        
                double correction = myPID.compute(0.1, error);

                feedback->vitesse_moteur = correction;

                goal_handle->publish_feedback(feedback);

                loop.sleep();

            }


        }


        






};

int main(int argc, char* argv[]){
    rclcpp::init(argc,argv);
    rclcpp::spin(make_shared<ActionServer>());
    rclcpp::shutdown();
    return 0;
}

