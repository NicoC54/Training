/**
 * Exercice 3 — Distance euclidienne 2D
 *
 * Calcule la distance géométrique en ligne droite entre la position
 * actuelle du drone (x1, y1) et le waypoint cible (x2, y2).
 *

 *
 * @param x1, y1 Coordonnées actuelles.
 * @param x2, y2 Coordonnées de la cible.
 * @return float Distance euclidienne.
 */

#include <cmath>
float compute_distance(float x1, float y1, float x2, float y2) {

    float dx = x1 - x2;
    float dy = y1 - y2;

    return std::sqrt(dx*dx + dy*dy);


    // À toi
}