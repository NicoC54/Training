#include <iostream>
#include <vector>
#include <algorithm> // Pour utiliser std::max

int max_poussee_continue(const std::vector<int>& fluctuations) {

    if (fluctuations.empty()){
        return 0;
    }

    int record = fluctuations[0];
    int score_actuel = fluctuations[0];

    for (int i = 1; i < fluctuations.size(); i++){

        score_actuel = std::max(fluctuations[i], score_actuel + fluctuations[i]);

        if (score_actuel > record){
            record = score_actuel;
        }
    }

    return record;
}






// --- BLOC DE TESTS ---
int main() {
    // Test 1 : La meilleure séquence continue est [4, -1, 2, 1]
    std::vector<int> test1 = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    std::cout << "Test 1 : " << max_poussee_continue(test1) << " (Attendu : 6)" << std::endl;

    // Test 2 : Que du positif
    std::vector<int> test2 = {1, 2, 3, 4, 5};
    std::cout << "Test 2 : " << max_poussee_continue(test2) << " (Attendu : 15)" << std::endl;

    // Test 3 : Que du négatif
    std::vector<int> test3 = {-5, -2, -9};
    std::cout << "Test 3 : " << max_poussee_continue(test3) << " (Attendu : -2)" << std::endl;

    // Test 4 : Edge Case (Tableau vide)
    std::vector<int> test4 = {};
    std::cout << "Test 4 : " << max_poussee_continue(test4) << " (Attendu : 0)" << std::endl;

    return 0;
}