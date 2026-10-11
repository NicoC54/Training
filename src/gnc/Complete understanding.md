Voici la version **ultime et définitive** de votre fiche résumé. Elle intègre désormais la dynamique temporelle du code (la boucle), l'origine matérielle/logicielle des données, et la justification mathématique de l'EKF par rapport au Kalman Linéaire.

C'est un véritable condensé d'expertise GNC (Guidance, Navigation, and Control).

---

# 🚀 Fiche Résumé GNC : Du Moteur au Filtre de Kalman (Version Ultime)

## 1. La Physique et le Contrôle (Mixer d'un Drone)

Le contrôleur PID ne raisonne pas en moteurs, mais en **physique des solides**. Il génère des commandes abstraites que la matrice de mixage traduit.

* **Lien PID / Physique :** Erreur de vitesse linéaire $\rightarrow$ Accélération linéaire $\rightarrow$ **Force** (Thrust sur Z). Erreur de vitesse angulaire $\rightarrow$ Accélération angulaire $\rightarrow$ **Couple/Torque** (Roll, Pitch, Yaw).
* **La Matrice de Mixage (+1 / -1) :**
* *Roulis/Tangage* : Se déduit par l'effet de levier (on accélère d'un côté, on ralentit l'autre).
* *Lacet (Yaw)* : Causé par la **résistance de l'air**. On accélère les moteurs qui tournent dans le sens *inverse* de la direction voulue. Les moteurs de même sens sont en diagonale.



## 2. Géométrie Spatiale : Repères et Matrices

* **Vecteurs (Forces, Vitesses) $\rightarrow$ Matrice 3x3 (Rotation) :** L'origine n'a pas d'importance (ex: IMU, Boussole).
* **Points (Coordonnées) $\rightarrow$ Matrice 4x4 (Homogène) :** Fusionne rotation et translation. Indispensable pour l'espace (ex: Lidar, Caméra).
* **L'astuce de la Matrice 3x3 :** Le "1" sur l'axe de rotation, les $\cos$ sur la diagonale, les $\sin$ restants. **L'axe Y est le rebelle** : son $-\sin$ est en bas à gauche, contrairement à X et Z.
* **La trinité de la rotation :** Pour une matrice 3x3, tourner dans l'autre sens, transposer, ou calculer l'inverse donne **exactement le même résultat**.

$$R(-\theta) = R^T = R^{-1}$$



## 3. D'où viennent les Coordonnées ? (Matériel vs Logiciel)

* **Le LOCAL (Instantané) = Le Matériel (Capteurs) :** Dans son repère, le robot est toujours à (0,0). Les coordonnées locales sont les positions instantanées des obstacles ou des forces lus par l'électronique (ex: Lidar détectant un mur à 3m).
* **Le GLOBAL (Intégré) = Le Logiciel (Odométrie / EKF) :** À part le GPS, aucun capteur ne donne de position absolue. Les coordonnées globales ($x_W, y_W, \theta_W$) sont une estimation mathématique maintenue en mémoire, calculée en cumulant les mouvements du robot depuis son point de départ.

## 4. La Boucle Temporelle du Filtre de Kalman (EKF)

Le Kalman est la "mémoire" du robot. Son état ($X$) vit TOUJOURS dans le Monde pour que l'intégration physique (accélération $\rightarrow$ vitesse $\rightarrow$ position) soit juste.

**La Boucle en 3 Étapes (100 à 500 fois/seconde) :**

1. **La Prédiction ($X_{pred}$) :** Le robot avance, on calcule sa nouvelle position théorique globale.
2. **L'Injection (Le cœur de l'EKF) :** On prend les chiffres de $X_{pred}$ et on les injecte dans les formules algébriques (les $\cos$ et $\sin$ de $H$). La matrice théorique devient une grille numérique concrète pour cet instant T.
3. **L'Update (La Correction) :** On compare la mesure réelle ($z$) avec la prédiction projetée ($h(X_{pred})$) pour corriger l'état global.

> **💡 Kalman Linéaire vs Étendu (EKF) :**
> * **Kalman Linéaire :** Géométrie fixe ou capteur absolu (GPS). La matrice $H$ ne contient que des constantes (0, 1...). Pas besoin de recalculer $H$ à chaque boucle.
> * **EKF :** Dès que le robot tourne librement, l'angle $\theta$ s'insère dans des $\cos$ et $\sin$. C'est une **non-linéarité**. On est obligé d'utiliser un EKF pour dériver ces équations (Jacobiennes) et recalculer $H$ à chaque milliseconde.
> 
> 

---

## 5. 🚨 DÉMARCHE CAPTEUR : Quand projeter une mesure ?

La question : **"Quel est le but de cette donnée ?"**

### Scénario A : Le but est le Filtre de Kalman

**$\rightarrow$ RÈGLE : NE JAMAIS PROJETER LA MESURE ($z$).** Tourner $z$, c'est tourner son bruit, ce qui détruit la stabilité.

1. **Garder $z$ dans son repère natif.**
2. **Créer $h(X)$ :** Projette l'état du Monde vers le **repère natif** du capteur.
* *Capteur Global (GPS) :* $h(X)$ pioche les variables. $H$ n'a que des 0 et 1.
* *Capteur Local Directionnel (IMU) :* $h(X)$ applique une **rotation inverse** ($R^T$ ou $-\theta$).
* *Capteur Local Spatial (Lidar) :* On doit ramener le monde au robot (distance) PUIS tourner. L'équation analytique magique (issue de la matrice 4x4 inversée) est :

$$P_{local} = R^T \cdot (P_{global} - T_{robot\_global})$$



*(Note: $T_{robot\_global}$ contient bien les coordonnées globales $x_W, y_W$ du robot).*


3. **Dériver pour obtenir la Jacobienne $H$.**

### Scénario B : Le but est la Cartographie / Contrôle (Hors Kalman)

**$\rightarrow$ RÈGLE : PROJETER LA MESURE ($z$) VERS LE MONDE.**

1. **Rotation directe :** Multipliez la mesure par la matrice avec l'angle actuel du robot (**$+\theta$**).
2. **Utiliser ROS (`tf2`) :** Laissez l'arbre de transformation faire ces multiplications mathématiques en tâche de fond pour éviter le Gimbal Lock (grâce aux quaternions).

---

## 6. La 2D n'est qu'une fraction de la 3D

* Un robot 2D ne gère mathématiquement ni le Pitch (tangage) ni le Roll (roulis) par manque d'axe Z.
* Le **Yaw (Lacet) en 3D est exactement le $\theta$ en 2D**.
* Gommez la 3ème ligne/colonne de la matrice 3D de lacet ($R_z$), vous obtenez l'unique matrice 2D.

## 7. Anti-sèches Mentales (Cheat Sheet)

* **Vecteur vs Point :** Vecteur = $3\times3$ (Rotation pure). Point = $4\times4$ (Rotation + Translation).
* **Le Piège 4x4 :** Pour inverser une matrice 4x4, on ne peut PAS juste mettre un angle $-\theta$ (cela n'inverse pas la position). Utilisez `matrice.inverse()` dans votre code. Pour les 3x3, utilisez `.transpose()`.
* **Le Piège du mot "Translation" :** Dans l'équation $R^T \cdot (P_{global} - T_{robot\_global})$, le vecteur $T$ désigne bien la position **globale** absolue du robot sur la carte ($x_W, y_W$).
* **Sens de Rotation :**
* Local vers Global = Angle direct $+\theta$.
* Global vers Local (Modèle EKF) = Angle inverse $-\theta$ (Transposée $R^T$).


* **Calculer une ligne de H :** Les variables d'état non impliquées dans l'équation $h(X)$ ont une dérivée de $0$.