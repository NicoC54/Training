#include <vector>

/* ======================================================================================
 * EXERCICE 1 : Filtre de Télémétrie et Détection d'Anomalies (25 min)
 * ======================================================================================
 * Contexte :
 * Lors d'une phase de vol, une sonde spatiale envoie des paquets de télémétrie contenant
 * son altitude. Malheureusement, le capteur est parfois sujet à des "glitches" 
 * (valeurs aberrantes).
 * 
 * Problème :
 * Implémentez une fonction qui filtre un flux de données selon le principe d'une moyenne 
 * mobile simple, et identifie les anomalies.
 * 
 * Règles :
 * - Étant donné un tableau d'altitudes `data`, une taille de fenêtre `window_size` et 
 *   un seuil `threshold` : Une altitude à l'index i est considérée comme une anomalie si sa 
 *   différence absolue avec la moyenne des `window_size` éléments précédents valides 
 *   (non-anormaux) est strictement supérieure à `threshold`.
 * - S'il y a moins de `window_size` éléments valides précédents, la moyenne est calculée 
 *   sur tous les éléments valides disponibles. 
 * - Le premier élément du tableau n'est jamais une anomalie.
 * 
 * Entrée / Sortie (Exemple) :
 * data = [10.0, 10.5, 11.2, 50.0, 11.5, 12.0]
 * window_size = 2, threshold = 5.0
 * Sortie attendue : [3] 
 * (car 50.0 diffère de la moyenne de [10.5, 11.2] = 10.85 de plus de 5.0. 
 * Il est donc ignoré pour les moyennes suivantes).
 * ====================================================================================== */

std::vector<int> findAnomalies(const std::vector<double>& data, int windowSize, double threshold) {

    if (data.empty()){
        return {};
    }

    std::vector<int> anormal_data;
    std::deque<double> fenetre_valide;

    fenetre_valide.push_back(data[0]);
    double somme_valeur_valide = data[0]

   
    for (int index_tete=1; index_tete < data.size(); index_tete++){

        double value_tested = data[index_tete];
        double moyenne = somme_valeur_valide / fenetre_valide.size();

        if (std::abs(value_tested - moyenne)>threshold){
            anormal_data.push_back(index_tete);
        }

        else {
            // On ajoute la nouvelle bonne valeur À LA FIN de la deque
            fenetre_valide.push_back(value_tested);
            somme_valeur_valide += value_tested;
        }

      
        if (fenetre_valide.size() > windowSize) {
                // On soustrait la plus vieille valeur (qui est au DÉBUT de la deque)
            somme_valeur_valide -= fenetre_valide.front(); 
                
                // Et on la détruit physiquement
            fenetre_valide.pop_front(); 
            
        }


    }

    return anormal_data;
}


#include <vector>

/* ======================================================================================
 * EXERCICE 2 : Planification de Pic de Consommation Électrique (35 min)
 * ======================================================================================
 * Contexte :
 * À bord d'un satellite, différentes tâches logicielles (calcul de trajectoire, allumage 
 * propulseur, transmission radio) s'exécutent sur des intervalles de temps précis et 
 * consomment une puissance donnée.
 * 
 * Problème :
 * Vous recevez une liste de tâches. Chaque tâche est définie par un tableau de 3 entiers : 
 * [start_time, end_time, power_consumption]. 
 * La tâche consomme son énergie du temps start_time (inclus) jusqu'au temps end_time (exclu).
 * Écrivez une fonction qui détermine la consommation électrique crête (le maximum de 
 * puissance consommée à un instant t donné).
 * 
 * Entrée / Sortie (Exemple) :
 * tasks = [[1, 5, 20], [3, 8, 15], [7, 10, 10], [4, 6, 5]]
 * Sortie attendue : 40
 * (Explication : Entre t=4 et t=5, les tâches [1,5,20], [3,8,15] et [4,6,5] tournent en 
 * même temps. 20 + 15 + 5 = 40).
 * ====================================================================================== */

int maxPowerPeak(const std::vector<std::vector<int>>& tasks) {
    // TODO: Ton code ici
    
    return 0;
}