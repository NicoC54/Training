#include <iostream>
#include <vector>

int recherche_dichotomique(const std::vector<int>& donnees, int cible) {

    // 1. Gérer le cas du tableau vide (Votre nouveau réflexe !)

    if (donnees.empty()) {
        return -1;
    }
    
    // 2. Initialiser les deux pointeurs aux extrémités
    int gauche = 0;
    int droite = donnees.size() - 1;

    // 3. Boucler tant que la zone de recherche est valide
    // (Tant que le pointeur gauche ne dépasse pas le pointeur droite)
    // while (...) {

    while (gauche <= droite){
        // a. Calculer l'index du milieu 
        // Formule ultra-sécurisée en C++ : int milieu = gauche + (droite - gauche) / 2;
        int milieu = gauche + (droite - gauche)/2;
        // b. Si la valeur à donnees[milieu] est la cible, bingo ! On retourne 'milieu'.
        if (donnees[milieu] == cible ){
            return milieu;
        }
        else if {donnees[milieu]<cible}{
            gauche = milieu +1;
        }
        else if {donnees[milieu]>cible}{
            droite = milieu - 1;
        }
    }
    
    return -1;
}

// --- BLOC DE TESTS ---
int main() {
    std::vector<int> donnees = {-1, 0, 3, 5, 9, 12};
    
    // Test 1 : Cible présente
    std::cout << "Test 1 : " << recherche_dichotomique(donnees, 9) << " (Attendu : 4)" << std::endl;

    // Test 2 : Cible absente
    std::cout << "Test 2 : " << recherche_dichotomique(donnees, 2) << " (Attendu : -1)" << std::endl;

    // Test 3 : Edge case (Tableau vide)
    std::vector<int> donnees_vides = {};
    std::cout << "Test 3 : " << recherche_dichotomique(donnees_vides, 5) << " (Attendu : -1)" << std::endl;

    return 0;
}