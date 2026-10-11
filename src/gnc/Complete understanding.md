Voici la fiche résumé mise à jour, avec une toute nouvelle section (la numéro 4) dédiée spécifiquement à **l'algorithme de décision face à une donnée capteur**. J'ai insisté sur la démarche pas à pas pour savoir quand et comment projeter une mesure.

---

# Fiche Résumé GNC : Du Moteur au Filtre de Kalman

## 1. La Physique et le Contrôle (Mixer d'un Drone)

Le contrôleur PID ne raisonne pas en nombre de moteurs, mais en **physique des solides**. Il génère des commandes abstraites que la matrice de mixage traduit pour le châssis physique.

* **Lien PID / Physique :** Erreur de vitesse linéaire $\rightarrow$ Accélération linéaire $\rightarrow$ **Force** (Thrust sur Z). Erreur de vitesse angulaire $\rightarrow$ Accélération angulaire $\rightarrow$ **Couple/Torque** (Roll, Pitch, Yaw).
* **La Matrice de Mixage (+1 / -1) :**
* *Roulis/Tangage* : Se déduit par l'effet de levier (on accélère d'un côté, on ralentit l'autre).
* *Lacet (Yaw)* : Causé par la **résistance de l'air**. On accélère les moteurs qui tournent dans le sens *inverse* de la direction voulue. Les moteurs de même sens sont toujours en diagonale.



## 2. Géométrie Spatiale : Repères et Matrices

La règle d'or pour passer d'un référentiel à l'autre est de comprendre la différence entre une direction et une coordonnée.

* **Vecteurs (Forces, Vitesses) $\rightarrow$ Matrice 3x3 (Rotation) :** L'origine (translation) n'a pas d'importance (ex: IMU, Boussole).
* **Points (Coordonnées) $\rightarrow$ Matrice 4x4 (Homogène) :** Fusionne la rotation et la translation. Indispensable pour la géométrie spatiale (ex: Lidar, Caméra).
* **L'astuce de la Matrice 3x3 :** Le "1" sur l'axe de rotation, les $\cos$ sur la diagonale, et les $\sin$ restants. **L'axe Y est le rebelle** : son $-\sin$ est en bas à gauche, contrairement à X et Z (en haut à droite).

## 3. L'Architecture du Filtre de Kalman (EKF)

Le Kalman est la "mémoire" du robot, il fusionne des capteurs aux repères natifs différents.

* **Le Vecteur d'État ($X$) vit TOUJOURS dans le Monde :** C'est indispensable pour que l'intégration mathématique (Accélération $\rightarrow$ Vitesse $\rightarrow$ Position) soit physiquement juste dans le temps.
* **La covariance (le bruit) dicte les règles :** Tourner mathématiquement une mesure brute, c'est aussi devoir tourner sa matrice de bruit, ce qui crée des instabilités. C'est pourquoi on préfère adapter la prédiction plutôt que la mesure.

---

## 4. 🚨 DÉMARCHE CAPTEUR : Quand projeter ou non une mesure ?

Face à une nouvelle donnée capteur (un obstacle Lidar, une accélération IMU), posez-vous toujours cette question : **"Quel est le but de cette donnée ?"**

### Scénario A : Le but est le Filtre de Kalman (Fusion de données)

**$\rightarrow$ RÈGLE : NE JAMAIS PROJETER LA MESURE ($z$).**

1. **Garder la mesure native :** Laissez $z$ dans son repère d'origine (le GPS reste en Monde, l'IMU/Radar/Odométrie reste en Local).
2. **Créer le traducteur $h(X)$ :** Écrivez l'équation géométrique qui projette l'état du Monde vers le point de vue du capteur.
* *Astuce géométrique :* On utilise la matrice de rotation avec l'angle inverse **$-\theta$** (ou la matrice transposée).


3. **Dériver pour obtenir $H$ :** Calculez la Jacobienne (les dérivées partielles) de $h(X)$ par rapport à chaque variable de l'état.
4. **Calculer l'erreur en local :** L'innovation se calcule via $z_{brut} - h(X_{monde})$. Le Kalman corrigera l'état Monde grâce à cette erreur purement locale.

### Scénario B : Le but est la Cartographie ou le Contrôle réactif (Hors Kalman)

**$\rightarrow$ RÈGLE : PROJETER LA MESURE ($z$) VERS LE MONDE.**
Si vous voulez afficher un point Lidar sur une carte (Mapping) ou compenser la gravité d'un accéléromètre brut, vous devez projeter la donnée.

1. **Identifier la nature de la donnée :** Vecteur (matrice 3x3) ou Point (matrice 4x4) ?
2. **Appliquer la rotation directe :** Multipliez la mesure par la matrice de rotation avec l'angle actuel du robot (**$+\theta$**).
* *Exemple Lidar :* $Point_{monde} = Matrice_{4x4} \cdot Point_{local\_Lidar}$
* *Exemple IMU (pour compenser la gravité) :* $Acc_{monde} = (Matrice_{3x3} \cdot Acc_{local\_IMU}) - Gravit\acute{e}$


3. **Utiliser ROS (tf2) si possible :** Au lieu de faire la multiplication à la main, laissez un arbre de transformation (via les quaternions) le faire pour vous, pour éviter le Gimbal Lock et bénéficier de l'interpolation temporelle.

---

## 5. La 2D n'est qu'une fraction de la 3D

* Un robot terrestre (2D) ne peut mathématiquement pas gérer le Pitch (tangage) ou le Roll (roulis), car il n'a pas d'axe Z.
* Le **Yaw (Lacet) en 3D est exactement le $\theta$ en 2D**.
* L'unique matrice de rotation 2D s'obtient simplement en gommant la 3ème ligne et la 3ème colonne de la matrice de lacet 3D ($R_z$).

## 6. Anti-sèches Mentales (Cheat Sheet)

* **Pour un problème de PID/Moteurs :** Visualisez une balançoire (Roll/Pitch) et pensez à la résistance de l'air sur les hélices (Yaw en diagonale).
* **De Local vers Global (Cartographie) :** Angle direct $+\theta$.
* **De Global vers Local (Modèle Kalman $H$) :** Angle inverse $-\theta$ (ou matrice transposée).
* **Calculer une ligne de H :** Posez l'équation trigonométrique naturelle $h(X)$, et dérivez isolément chaque variable ($x, y, \theta, v...$). Les variables non impliquées deviennent des $0$.