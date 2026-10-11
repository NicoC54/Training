# Les Fondamentaux du GNC pour la Robotique Mobile

Ce document résume les concepts mathématiques et physiques de base essentiels pour un ingénieur GNC (Guidance, Navigation, and Control) junior, en se concentrant sur la robotique mobile terrestre (2D).

---

## 1. Repères Spatiaux et Matrices de Transformation

En robotique mobile, le problème de la localisation se simplifie généralement à un environnement en deux dimensions (2D). Il est crucial de maîtriser le passage entre le repère local du robot et le repère global de la carte.

### Les deux repères principaux
*   **Le repère Global (World - $W$) :** Il s'agit du repère fixe de la carte. Son origine $(0,0)$ est arbitraire (souvent le point de départ du robot).
*   **Le repère Local (Robot - $R$) :** Ce repère est mobile, attaché au centre du robot. Par convention, l'axe X pointe toujours vers "l'avant" du robot, et l'axe Y vers sa gauche.

### Le vecteur d'état (La Pose)
À tout instant, la position et l'orientation du robot dans le repère global sont définies par son vecteur d'état, appelé sa "pose" :

$$P_W = \begin{bmatrix} x \\ y \\ \theta \end{bmatrix}$$

Où :
*   $x$ et $y$ représentent les coordonnées cartésiennes.
*   $\theta$ (thêta) est le cap (yaw), c'est-à-dire l'angle entre l'axe X du monde global et l'axe X du robot.

### Le changement de repère (Transformation Homogène)
Pour traduire les coordonnées d'un point (par exemple, un obstacle détecté par un capteur) du repère local du robot vers le repère global du monde, on utilise une matrice de transformation homogène. Cette matrice combine la **rotation** (alignement des axes) et la **translation** (déplacement de l'origine).

Soit un point $P_R$ détecté dans le repère du robot. Sa position dans le monde global $P_W$ est calculée par :

$$P_W = T_W^R \cdot P_R$$

Sous forme matricielle, en utilisant les coordonnées homogènes (ajout d'un `1` à la fin des vecteurs pour permettre la translation par multiplication), cela s'écrit :

$$ \begin{bmatrix} x_{monde} \\ y_{monde} \\ 1 \end{bmatrix} = \begin{bmatrix} \cos(\theta) & -\sin(\theta) & x_{robot} \\ \sin(\theta) & \cos(\theta) & y_{robot} \\ 0 & 0 & 1 \end{bmatrix} \cdot \begin{bmatrix} x_{point\_local} \\ y_{point\_local} \\ 1 \end{bmatrix} $$

---

## 2. Cinématique Simple : Différentiel et Bicyclette

La cinématique est la discipline qui relie les commandes envoyées aux actionneurs (les moteurs) au mouvement géométrique global du robot (vitesse linéaire $V$ et vitesse angulaire $\omega$).

### A. Le robot à entraînement différentiel
C'est l'architecture la plus répandue en robotique de service (ex: TurtleBot, robots aspirateurs). Le robot possède deux roues motrices indépendantes disposées sur le même axe.

*   **Variables du modèle :**
    *   $v_D$ : Vitesse de la roue droite
    *   $v_G$ : Vitesse de la roue gauche
    *   $L$ : Entraxe (distance séparant les deux roues)

*   **Équations fondamentales :**
    *   La vitesse linéaire globale du robot ($V$) est la moyenne des vitesses des deux roues :
        $$V = \frac{v_D + v_G}{2}$$
    *   La vitesse angulaire du robot ($\omega$) est proportionnelle à la différence de vitesse des roues :
        $$\omega = \frac{v_D - v_G}{L}$$

*   **Comportement :**
    *   Si $v_D = v_G$ : Mouvement rectiligne pur ($V > 0$, $\omega = 0$).
    *   Si $v_D = -v_G$ : Rotation pure sur place ($V = 0$, $\omega \neq 0$).

### B. Le modèle bicyclette (Véhicule type Ackermann)
Contrairement au robot différentiel, une voiture classique est soumise à des contraintes non holonomes (elle ne peut pas se déplacer latéralement ni tourner sur place). On modélise souvent ce système par un "vélo" : une roue arrière propulsive et une roue avant directrice.

*   **Variables du modèle :**
    *   $V$ : Vitesse de propulsion (roue arrière)
    *   $L$ : Empattement (distance entre l'essieu avant et arrière)
    *   $\delta$ : Angle de braquage de la roue avant

*   **Équations fondamentales :**
    *   La vitesse de translation du centre du véhicule correspond directement à $V$.
    *   La vitesse angulaire ($\omega$) de rotation du châssis est contrainte par l'angle de braquage et la vitesse d'avancement :
        $$\omega = \frac{V}{L} \cdot \tan(\delta)$$

*   *Note importante :* Dans ce modèle, si le véhicule est à l'arrêt ($V = 0$), sa vitesse angulaire est obligatoirement nulle ($\omega = 0$), quelle que soit la valeur de braquage $\delta$.

---

## 3. Mise à jour de l'état : L'Odométrie
Une fois les vitesses $V$ et $\omega$ calculées par le modèle cinématique, le robot doit intégrer ces vitesses dans le temps pour mettre à jour sa position sur la carte. C'est le principe de l'odométrie (par la méthode d'Euler).

À chaque pas de temps $\Delta t$ de la boucle de contrôle, les nouvelles coordonnées se calculent ainsi :

$$x_{nouveau} = x_{ancien} + V \cdot \cos(\theta_{ancien}) \cdot \Delta t$$
$$y_{nouveau} = y_{ancien} + V \cdot \sin(\theta_{ancien}) \cdot \Delta t$$
$$\theta_{nouveau} = \theta_{ancien} + \omega \cdot \Delta t$$