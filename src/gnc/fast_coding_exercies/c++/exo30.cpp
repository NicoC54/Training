#include <vector>
#include <iostream>

class ConstructionGame {
private:
    

public:
    // 1. Le constructeur
    ConstructionGame(int length, int width) {

        table = std::vector<std::vector<int>>(length, std::vector<int>(width, 0));
    }

    // 2. La fonction addCubes
    void addCubes(const std::vector<std::vector<bool>>& cubes) {
        for (int i =0; i< cubes.size(); i++){
            for (int j = 0; j <cubes[0].size(); j++){
                if (cubes[i][j] == true){
                    table[i][j] = table[i][j] + 1;
                }
            }

        }
    }

    // 3. La méthode getHeight
    int getHeight() {
        int max_height = 0;
        for (int i=0; i<table.size(); i++){
            for (int j = 0; j <table[0].size(); j++){
                int actual_height = table[i][j];
                
                if (actual_height > max_height){
                    max_height = actual_height;
                }
                }

        }
        
        return max_height; 
    }

private:

    std::vector<std::vector<int>> table;
};