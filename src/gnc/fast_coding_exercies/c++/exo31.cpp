#include <vector>
#include <iostream>

class VegetableGarden {
public:
    // 1. Le constructeur
    VegetableGarden(int rows, int cols) {
        // À compléter : initialiser le terrain avec des 0
        terrain = std::vector<std::vector<int>>(rows, std::vector<int>(cols,0));

        
    }

    // 2. Semer des graines (comme addCubes)
    void sowSeeds(const std::vector<std::vector<bool>>& seeds) {
        for (int i = 0; i < seeds.size(); i++ ){
            for (int j = 0; j < seeds[0].size(); j++){
                if (seeds[i][j] == true){
                    terrain[i][j] += 1;
                }
            }
        }
        
    }

    // 3. Arroser une ligne spécifique (NOUVEAUTÉ)
    void waterRow(int rowIndex) {
        for (int i = 0, i < terrain[0].size(); i++){
            terrain[rowIndex][i] += 1;
        }
        
    }

    // 4. Compter le total (NOUVEAUTÉ)
    int getTotalPlants() {
        int total = 0;
         for (int i = 0; i < terrain.size(); i++ ){
            for (int j = 0; j < terrain[0].size(); j++){
                total += terrain[i][j];
    }
    return total;
}

private:
    std::vector<std::vector<int>> terrain;
};