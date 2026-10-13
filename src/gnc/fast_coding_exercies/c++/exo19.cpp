#include <iostream>
#include <vector>

int pic_de_signal(const std::vector<int>& signaux, int k) {

    if (signaux.size() < k){
        return 0;
    }

    int somme_totale = 0;
    int somme_max = 0;
    int start_indice = 0;

    for (int i = 0 ; i < k; i++ ){
        somme_totale += signaux[i];
    }

    somme_max = somme_totale;

    for (int i = k; i < signaux.size(); i++){

        somme_totale -= signaux[start_indice];
        start_indice++;
        somme_totale += signaux[i];

        if (somme_totale > somme_max){
            somme_max = somme_totale;
        }

    }

    return somme_max;

   
}

// --- BLOC DE TESTS ---
int main() {
    // Test 1 : Cas classique
    std::vector<int> test1 = {2, 1, 5, 1, 3, 2};
    std::cout << "Test 1 : " << pic_de_signal(test1, 3) << " (Attendu : 9)" << std::endl;

    // Test 2 : Fenêtre très large avec des nombres négatifs
    std::vector<int> test2 = {1, 9, -1, -2, 7, 3, -1, 2};
    std::cout << "Test 2 : " << pic_de_signal(test2, 4) << " (Attendu : 13)" << std::endl;

    // Test 3 : Tableau trop petit
    std::vector<int> test3 = {5, 2};
    std::cout << "Test 3 : " << pic_de_signal(test3, 3) << " (Attendu : 0)" << std::endl;

    return 0;
}