/**
 * Exercice 5 — Normalisation d'angle
 *
 * Ramène un angle exprimé en radians dans l'intervalle [-pi, pi].
 *
 * Astuce classique en navigation : 
 * atan2(sin(a), cos(a)) gère automatiquement le repliement sur [-pi, pi].
 * Fonctions de <cmath> : std::atan2, std::sin, std::cos.
 *
 * @param angle_rad Angle brut en radians.
 * @return float    Angle normalisé dans [-pi, pi].
 */
float normalize_angle(float angle_rad) {
    float pi = 3.14;

    while (angle_rad < -pi){
        angle_rad = angle_rad + 2*pi;
        }
    while (angle_rad > pi){
        angle_rad = angle_rad - 2*pi;
        }

        return angle_rad;
    }

  