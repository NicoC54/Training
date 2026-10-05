

class Astar{

    public:

        Astar(int cols, int lines, std::vector<int> grid1D) : nb_cols(cols), nb_lines(lines), grid(grid1D){}


        std::vector<int> ConstructPath(int index, std::vector<int> parents){

            std::vector<int> path;
            
            while (index!=-1){
                path.push_back(index);
                index = parents[index];
            }
            std::reverse(path.begin(), path.end());
            return path;
        }

        
        int getX(int index){
            return index%nb_cols;
        }
        int getY(int index){
            return index/nb_cols;

        }
        int getIndex(int x, int y){
            return y*nb_cols + x;
        }

        std::vector<int> GetNeighbors(int index){

            std::vector<int> neighbors;

            int current_x = getX(index);
            int current_y = getY(index);

            // attention à bien mettre le getIndex

            if (current_x > 0){
                neighbors.push_back(getIndex(current_x-1,current_y));
            }
            if (current_x < nb_cols - 1){
                neighbors.push_back(getIndex(current_x+1,current_y));
            }
            //attention a bien mettre le nb_lines
            if (current_y >0){
                neighbors.push_back(getIndex(current_x,current_y-1));
            }
            if (current_y < nb_lines - 1){
                neighbors.push_back(getIndex(current_x,current_y+1));
            }
            return neighbors;
        }

        double heuristique(int starting_node, int ending_node){

            double dx = getX(starting_node) - getX(ending_node);
            double dy = getY(starting_node) - getY(ending_node);
            return std::abs(dx) + std::abs(dy);
        }


        std::vector<int> Compute(int starting_node, int ending_node, std::vector<int> grid){

            double INF = 1e4;
            std::vector<int> parents(grid.size(),-1);
            std::vector<int> gscores(grid.size(),INF);

            using Pair = std::pair<double, int>;

            std::priority_queue<Pair, std::vector<Pair>, std::greater<Pair>> pq;

            gscores[starting_node] = 0;

            double f_score_inital = heuristique(starting_node,ending_node);
            pq.push({f_score_inital, starting_node});

            while (!pq.empty()){
                auto [current_f_score, current_node] = pq.top();
                pq.pop();

                if (current_node == ending_node){
                    //attention à mettre le parents
                    return ConstructPath(current_node, parents);
                }
                best_f_score = gscores[current_node] + heuristique(current_node, ending_node);
                if (current_f_score > best_f_score ){
                    continue;
                }
                std::vector<int> neighbors = getNeighbors(current_node);

                for (auto neighbor : neighbors) {

                    if (grid[neighbor]==100) {
                        continue;
                    }

                    double neighbor_gscore = gscores[current_node] + 1;
                    if (neighbor_gscore < gscores[neighbor]){
                         gscores[neighbor] = neighbor_gscore;
                         parents[neighbor] = current_node;
                         double neighbor_f_score = heuristique(neighbor, ending_node) + gscores[neighbor];
                         pq.push({neighbor_f_score,neighbor});
                    }
                }

                
            }

            return {};
        }

    private:

        int nb_cols;
        int nb_lines;
        std::vector<int> grid;

        
    };


    class Service : rclcpp::Node{

        public :
        
            Service() : Node("Service_node"){

            service_ = this->create_service<package_name::srv::Struct_name>("topic_service", [this](std::shared_ptr<package_name::srv::Request> request, std::shared_ptr<package_name::srv::Response> response ){this->callbackService(request, response)});



        }

        private:

            rclcpp::Service<package_name::srv::GetPath>::SharedPtr service_;

            callbackService(std::shared_ptr<package_name::srv::Request> request, std::shared_ptr<package_name::srv::Response> response){
            int nb_cols = request-> width;
            int nb_lines = request-> height;
            std::vector<int> grid = request-> grid;
            int starting_node = request -> start_node;
            int ending_node = request ->goal_node;

            Astar myAstar(nb_cols,nb_lines,grid);
            response -> path = myAstar.compute(starting_node,ending_node,grid);
            
        }
        
        
        }





    
