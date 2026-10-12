/**
 * Exercice 4 — Intégration temporelle (Euler explicite)
 *
 * Met à jour la position 1D d'un véhicule à partir de sa vitesse actuelle
 * et du pas de temps écoulé (dt).
 *
 * Spécifications :
 * - Sécurité temporelle : si dt <= 0.0f, la position ne doit pas changer
 *   (ignorer le pas de temps invalide et retourner pos_actuelle).
 *
 * @param current_pos Position actuelle (m).
 * @param velocity    Vitesse courante (m/s).
 * @param dt          Pas de temps écoulé (s).
 * @return float      Nouvelle position (m).
 */
float update_position_euler(float current_pos, float velocity, float dt) {

        if (dt < 0){
            return current_pos;
        }

        current_pos = current_pos + velocity*dt;

        return current_pos;
    // À toi
}