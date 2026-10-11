# Fiche Résumé GNC : Du Moteur au Filtre de Kalman

## 1. La Physique et le Contrôle (Mixer d'un Drone)

Le contrôleur PID ne raisonne pas en nombre de moteurs, mais en **physique des solides**. Il génère des commandes abstraites que la matrice de mixage traduit pour le châssis physique.

* **Lien PID / Physique :** Erreur de vitesse linéaire $\rightarrow$ Accélération linéaire $\rightarrow$ **Force** (Thrust sur Z). Erreur de vitesse angulaire $\rightarrow$ Accélération angulaire $\rightarrow$ **Couple/Torque** (Roll, Pitch, Yaw).
* **La Matrice de Mixage (+1 / -1) :**
* *Roulis/Tangage* : Se déduit par l'effet de levier (on accélère d'un côté, on ralentit l'autre).
* *Lacet (Yaw)* : Causé par la **résistance de l'air**. On accélère les moteurs qui tournent dans le sens *inverse* de la direction voulue (pour utiliser leur couple de réaction). Les moteurs de même sens sont toujours en diagonale.



## 2. Géométrie Spatiale : Repères et Matrices

La règle d'or pour passer d'un référentiel à l'autre est de comprendre la différence entre une direction et une coordonnée.

* **Vecteurs (Forces, Vitesses) $\rightarrow$ Matrice 3x3 (Rotation) :** L'origine (translation) n'a pas d'importance (ex: IMU, Boussole).
* **Points (Coordonnées) $\rightarrow$ Matrice 4x4 (Homogène) :** Fusionne la rotation et la translation en une seule opération. Indispensable pour la géométrie spatiale (ex: Lidar, Caméra).
* **L'astuce de la Matrice 3x3 :** Le "1" sur l'axe de rotation, les $\cos$ sur la diagonale principale, et les $\sin$ restants. **L'axe Y est le rebelle** : à cause du cycle naturel des axes, son $-\sin$ est en bas à gauche, contrairement à X et Z (en haut à droite).
* **La trinité mathématique de la rotation :** Pour une matrice de rotation pure (3x3), tourner dans l'autre sens, transposer les lignes/colonnes, ou calculer l'inverse donne **exactement le même résultat**.

$$R(-\theta) = R^T = R^{-1}$$



## 3. L'Architecture du Filtre de Kalman (EKF)

Le Kalman est la "mémoire" du robot, il fusionne des capteurs aux repères natifs différents.

* **Le Vecteur d'État ($X$) vit TOUJOURS dans le Monde :** C'est indispensable pour que l'intégration mathématique (Accélération $\rightarrow$ Vitesse $\rightarrow$ Position) soit physiquement juste dans le temps par rapport à un référentiel fixe (inertiel).
* **La covariance (le bruit) dicte les règles :** Tourner mathématiquement une mesure brute, c'est aussi devoir tourner sa matrice de bruit, ce qui crée des instabilités numériques majeures. C'est pourquoi on préfère adapter la prédiction plutôt que la mesure.

---

## 4. 🚨 DÉMARCHE CAPTEUR : Quand projeter ou non une mesure ?

Face à une nouvelle donnée capteur, la question est : **"Quel est le but de cette donnée ?"**

### Scénario A : Le but est le Filtre de Kalman (Fusion de données)

**$\rightarrow$ RÈGLE : NE JAMAIS PROJETER LA MESURE ($z$).** L'innovation se fait toujours dans le repère natif du capteur ($y = z - h(X)$).

1. **Garder la mesure native :** Laissez $z$ dans son repère d'origine.
2. **Créer le traducteur $h(X)$ :** Son rôle est de projeter l'état du Monde vers le **repère natif** du capteur.
* **Cas 1 : Capteur Natif Global (GPS).** $h(X)$ extrait juste les variables (ex: $h(X) = [x_W, y_W]^T$). La matrice $H$ ne contiendra que des 0 et des 1.
* **Cas 2 : Capteur Natif Local Directionnel (IMU).** $h(X)$ applique une **rotation inverse** ($R^T$ ou angles négatifs) pour tourner l'état mondial.
* **Cas 3 : Capteur Natif Local Spatial (Lidar).** $h(X)$ doit appliquer l'inverse d'une transformation homogène.
* *Méthode 1 (L'équation décomposée, idéale pour dériver H) :* $P_{local} = R^T \cdot (P_{global} - T_{robot})$
* *Méthode 2 (La matrice 4x4 globale) :* $P_{local} = H^{-1} \cdot P_{global}$
* ⚠️ **LE PIÈGE 4x4 :** On ne peut PAS juste mettre un angle négatif dans une matrice 4x4 normale, car cela n'inverse pas la translation. Il faut calculer la vraie matrice inverse :

$$H^{-1} = \begin{bmatrix} R^T & -R^T \cdot T_{robot} \\ 0 & 1 \end{bmatrix}$$






3. **Dériver pour obtenir $H$ :** Calculez la Jacobienne (dérivées partielles) de l'équation $h(X)$ par rapport à chaque variable de l'état.

### Scénario B : Le but est la Cartographie ou le Contrôle réactif (Hors Kalman)

**$\rightarrow$ RÈGLE : PROJETER LA MESURE ($z$) VERS LE MONDE.**

1. **Identifier la nature de la donnée :** Vecteur (matrice 3x3) ou Point (matrice 4x4) ?
2. **Appliquer la rotation directe :** Multipliez la mesure par la matrice avec l'angle actuel du robot (**$+\theta$**).
* *Exemple Lidar :* $Point_{monde} = Matrice_{4x4} \cdot Point_{local\_Lidar}$
* *Exemple IMU (compenser la gravité) :* $Acc_{monde} = (Matrice_{3x3} \cdot Acc_{local\_IMU}) - Gravit\acute{e}$


3. **Utiliser ROS (tf2) :** Laissez l'arbre de transformation (`tf2`) faire ces multiplications complexes en tâche de fond pour éviter le Gimbal Lock.

---

## 5. La 2D n'est qu'une fraction de la 3D

* Un robot terrestre (2D) ne peut mathématiquement pas gérer le Pitch (tangage) ou le Roll (roulis), car il n'a pas d'axe Z.
* Le **Yaw (Lacet) en 3D est exactement le $\theta$ en 2D**.
* L'unique matrice de rotation 2D s'obtient simplement en gommant la 3ème ligne et la 3ème colonne de la matrice de lacet 3D ($R_z$).

## 6. Anti-sèches Mentales (Cheat Sheet)

* **Pour un problème PID :** Visualisez une balançoire (Roll/Pitch) et pensez à la "mélasse" de l'air sur les hélices (Yaw en diagonale).
* **Vecteur (Vitesse/Acc) vs Point (Position) :** Vecteur = $3\times3$ (Rotation pure). Point = $4\times4$ (Rotation + Translation).
* **Sens de Rotation :**
* Local vers Global (Cartographie) = Angle direct $+\theta$.
* Global vers Local (Modèle Kalman $H$) = Angle inverse $-\theta$ (Transposée $R^T$).


* **L'équation spatiale magique du Kalman :** On soustrait d'abord les positions pour avoir le vecteur distance absolu, PUIS on tourne le vecteur obtenu : $R^T \cdot (P_{global} - T_{robot})$.
* **L'astuce de l'inversion :** Dans le code, pour inverser une rotation 3x3, utilisez `.transpose()` (instantané) plutôt que `.inverse()` (plus lourd).
* **Calculer une ligne de H :** Les variables non impliquées dans $h(X)$ ont une dérivée de $0$. Les variables trigonométriques créent des lignes de $\cos$ et $\sin$.