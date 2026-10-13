#include <iostream>
#include <vector>

void nettoyer_telemetrie(std::vector<int>& paquets) {

    

   

}

// --- BLOC DE TESTS (Fonction utilitaire pour l'affichage) ---
void afficher(const std::vector<int>& v) {
    std::cout << "[";
    for (size_t i = 0; i < v.size(); i++) {
        std::cout << v[i] << (i < v.size() - 1 ? ", " : "");
    }
    std::cout << "]\n";
}

int main() {
    // Test 1 
    std::vector<int> test1 = {0, 1, 0, 3, 12};
    nettoyer_telemetrie(test1);
    std::cout << "Test 1 : "; afficher(test1); // Attendu : [1, 3, 12, 0, 0]

    // Test 2 
    std::vector<int> test2 = {0, 0, 0};
    nettoyer_telemetrie(test2);
    std::cout << "Test 2 : "; afficher(test2); // Attendu : [0, 0, 0]

    // Test 3 
    std::vector<int> test3 = {4, 2, 8};
    nettoyer_telemetrie(test3);
    std::cout << "Test 3 : "; afficher(test3); // Attendu : [4, 2, 8]

    return 0;
}