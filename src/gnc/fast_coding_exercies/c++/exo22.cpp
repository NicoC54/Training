#include <iostream>
#include <vector>
// Vous pouvez inclure <algorithm> si vous souhaitez utiliser std::max et std::min

int max_gain_energie(const std::vector<int>& niveaux) {

    if (niveaux.empty()){
        return 0;
    }

    int minimum = niveaux[0];
    int ecart_max = 0;

    for (int i = 1; i < niveaux.size(); i++){

        if (niveaux[i] < minimum){
            minimum = niveaux[i];
        }

        else {
            int ecart = niveaux[i] - minimum;

            if (ecart > ecart_max){
                ecart_max = ecart;
            }

        }
    }

    if (ecart_max != 0){ //si on fait que decroitre o nrentre dans niveaux[i] < minimum
        return ecart_max;
    }

    // ---------------------------------
    // VOTRE CODE ICI
    // ---------------------------------

    return 0;
}

// --- BLOC DE TESTS ---
int main() {
    // Test 1 : Cas classique
    std::vector<int> test1 = {7, 1, 5, 3, 6, 4};
    std::cout << "Test 1 : " << max_gain_energie(test1) << " (Attendu : 5)" << std::endl;

    // Test 2 : Chute libre continue, aucun gain possible
    std::vector<int> test2 = {7, 6, 4, 3, 1};
    std::cout << "Test 2 : " << max_gain_energie(test2) << " (Attendu : 0)" << std::endl;

    // Test 3 : Tableau trop petit
    std::vector<int> test3 = {5};
    std::cout << "Test 3 : " << max_gain_energie(test3) << " (Attendu : 0)" << std::endl;

    return 0;
}