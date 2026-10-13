#include <iostream>
#include <vector>
#include <algorithm> // Pour std::max

int max_requests(const std::vector<int>& timestamps, int window_size) {

    int index_queue = 0;
    int number_max_values = 0;

    if (timestamps.empty()){
        return 0;
    }

    for (int index_tete = 0 ; index_tete < timestamps.size(); index_tete++){

        while(timestamps[index_tete] - timestamps[index_queue] > window_size) {
            index_queue ++;
        }

        int number_correct_values = index_tete - index_queue +1;

        if (number_correct_values > number_max_values){
            number_max_values = number_correct_values;
        }

    }

    return number_max_values;
}

// --- BLOC DE TESTS ---
int main() {
    // Test 1 : Cas classique
    std::vector<int> test1 = {1, 5, 5, 8, 12, 13, 14, 15};
    std::cout << "Test 1 : " << max_requests(test1, 5) << " (Attendu : 4)" << std::endl;

    // Test 2 : Edge Case (Tableau vide)
    std::vector<int> test2 = {};
    std::cout << "Test 2 : " << max_requests(test2, 5) << " (Attendu : 0)" << std::endl;

    // Test 3 : Fenêtre très petite
    std::vector<int> test3 = {1, 2, 8, 8, 8, 9};
    std::cout << "Test 3 : " << max_requests(test3, 1) << " (Attendu : 4)" << std::endl; 
    // Explication Test 3 : les requêtes à {8, 8, 8, 9} rentrent dans une fenêtre de 1 seconde (9 - 8 <= 1).

    return 0;
}