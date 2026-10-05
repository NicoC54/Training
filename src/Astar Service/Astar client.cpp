class Client : rclcpp::Node {


    public:

        Client() : Node("CLient"){

            client_ = this->create_client<nom_pkg::srv::nom_struct>("nom_topic");


        }

        void sendRequest(){


            while (!client->wait_for_service(std::chrono::milliseconds(1000))){
                RCLCCP_INFO(this->get_logger();"en attente du serveur, reessai");
            }
            auto request = std::make_shared<nom_pkg::srv::nom_struct::Request>();

            // la on remplit le request : request -> width = 3 etc....


            //une fois fini on déclare un future

            using Future = std::shared_ptr<nom_pkg::srv::nom_struct>::SharedFuture;

            auto lambda = [this](Future future){
                auto response = future.get();
                std::cout << "réponse recue, la réponse est : " <<std::endl;
                for (int index : response -> path){
                    std:: cout << index <<std::endl;
                }
            }

            client_ -> async_send_request(request, lambda);



        }

    private: 
        
        std::shared_ptr<rclcpp::Client<nom_pkg::srv::nom_struct>> client_;
}


int main (int argc, char* argv[]){
    rclcpp::init(argc,argv);
    auto node = std::make_shared<Client>();
    node -> sendRequest();
    rclcpp::spin(node);
    rclcpp::shutdown();
}