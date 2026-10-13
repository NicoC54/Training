#include <iostream>
#include <vector>

int compter_mesures_sous_seuil(const std::vector<int>& altitudes, int seuil) {

    if (altitudes.empty()){
        return 0;
    }

    index_gauche = 0;
    index_droite = altitudes.size() - 1;

    while (index_gauche <= index_droite){
        
        int index_milieu = index_gauche + (index_droite-index_gauche) / 2;

       
        if (altitudes[index_milieu] < seuil){
            index_gauche = index_milieu + 1;
        }
        else{
            index_droite = index_milieu - 1;
        }

    }
   
    
    return index gauche;
}

// --- BLOC DE TESTS ---
int main() {
    // Test 1 : Cas nominal
    std::vector<int> alt1 = {100, 250, 400, 600, 900};
    std::cout << "Test 1 : " << compter_mesures_sous_seuil(alt1, 400) << " (Attendu : 2)" << std::endl;

    // Test 2 : Seuil plus bas que toutes les valeurs
    std::vector<int> alt2 = {200, 300, 500};
    std::cout << "Test 2 : " << compter_mesures_sous_seuil(alt2, 100) << " (Attendu : 0)" << std::endl;

    // Test 3 : Seuil plus haut que toutes les valeurs
    std::vector<int> alt3 = {50, 80, 120};
    std::cout << "Test 3 : " << compter_mesures_sous_seuil(alt3, 500) << " (Attendu : 3)" << std::endl;

    // Test 4 : Edge case - Tableau vide
    std::vector<int> alt4 = {};
    std::cout << "Test 4 : " << compter_mesures_sous_seuil(alt4, 300) << " (Attendu : 0)" << std::endl;

    return 0;
}