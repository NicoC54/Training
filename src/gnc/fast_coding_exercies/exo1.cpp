/**
 * Exercice 1 — Rejet de valeurs aberrantes (Outlier Rejection)
 *
 * Calcule la moyenne arithmétique des mesures de distance valides.
 *
 * Spécifications :
 * - Une mesure x est valide ssi 0.0 < x <= 10.0.
 * - Les valeurs hors plage doivent être ignorées.
 * - Si aucune mesure valide n'est trouvée, retourner 0.0f.
 *
 * @param mesures Vecteur de mesures brutes du capteur.
 * @return float  Moyenne des mesures valides, ou 0.0f si aucune valide.
 */
float compute_filtered_mean(const std::vector<float>& mesures) {

    int mesure_valide = 0;
    float somme = 0;

    for (const float mesure : mesures){

        if (mesure <= 0){
            continue;
        }

        if (mesure > 10){
            continue;
        }

        mesure_valide ++;
        somme += mesure;
    }

    if (mesure_valide >= 1){
        return somme/mesure_valide;
    }

    else {
        return 0.0f;
    }



  
}