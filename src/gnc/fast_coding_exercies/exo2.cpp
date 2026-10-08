#include <algorithm>
/**
 * Exercice 2 — Contrôleur P avec Saturation
 *
 * Calcule la commande moteur issue d'un gain proportionnel 
 * et sature la sortie entre [-max_cmd, max_cmd].
 *
 * Spécifications :
 * - commande_brute = Kp * error
 * - Si commande_brute > max_cmd, saturer à max_cmd.
 * - Si commande_brute < -max_cmd, saturer à -max_cmd.
 * - On suppose max_cmd > 0.0f.
 *
 * @param error    Écart entre la consigne et la mesure.
 * @param Kp       Gain proportionnel.
 * @param max_cmd  Limite maximale absolue autorisée.
 * @return float   Commande saturée finale.
 */
float compute_motor_cmd(float error, float Kp, float max_cmd) {
    // À toi de jouer

    float correction = Kp*error;

    if (correction > max_cmd){
        correction = max_cmd;
    }
    if (correction < -max_cmd){
        correction = -max_cmd;
    }

    return correction;
    
}