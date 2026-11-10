"""
ex13 — Container With Most Water   (LeetCode medium, pattern TWO POINTERS)

ÉNONCÉ
  On te donne une liste `height` de hauteurs (des entiers >= 0).
  Chaque hauteur est une barre verticale à l'indice i, de hauteur height[i].
  Deux barres + l'axe horizontal forment un récipient qui retient de l'eau.
  La quantité d'eau entre les barres i et j (i < j) vaut :
        largeur * hauteur = (j - i) * min(height[i], height[j])
  (l'eau déborde par la barre la PLUS BASSE, d'où le min)
  Trouve la quantité d'eau MAXIMALE qu'on peut retenir. Retourne un entier.

EXEMPLE
  height = [1,8,6,2,5,4,8,3,7]  -> 49
     (entre l'indice 1 (hauteur 8) et l'indice 8 (hauteur 7) :
      largeur = 8-1 = 7, hauteur = min(8,7) = 7, aire = 7*7 = 49)

CONTRAINTES
  - 2 <= len(height) <= 10^5
  - 0 <= height[i]

IDÉE DU PATTERN (two pointers)
  - Un pointeur `left` au début, un pointeur `right` à la fin.
  - À chaque étape, calcule l'aire entre eux et garde le max.
  - Puis déplace le pointeur qui pointe la barre la PLUS BASSE (vers l'intérieur).
    Pourquoi la plus basse ? Parce que c'est elle qui limite la hauteur (le min).
    Bouger la plus haute ne peut que réduire l'aire ; bouger la plus basse
    est la seule chance de trouver mieux.
  - On s'arrête quand left et right se croisent.
  -> O(n) : chaque barre est vue une fois. (la force brute O(n^2) teste toutes
     les paires -> trop lent)

CONSIGNE DE DRILL (conditions Thalanor : solo, sans IA, sans autocomplétion)
  1. Lis l'énoncé DEUX fois. Type de retour ? (un entier = aire max)
  2. Déroule À LA MAIN [1,8,6,2,5,4,8,3,7] sur 2-3 étapes : qui bouge, pourquoi ?
  3. Version two-pointers directement (la brute force O(n^2) est hors sujet ici).
  4. Donne la complexité à la fin.

Écris ton code, puis lance :  python3 ex13_container_water.py
"""


def max_area(height):

    left = 0
    right = len(height)-1
    max_area = 0

    while (left <= right):
        area = min(height[left], height[right]) * (right - left)
        if area > max_area:
            max_area = area

        if height[left] > height[right]:
            right -=1

        else:
            left+=1

    return max_area


        
    
   


# --- tests (ne pas modifier) -------------------------------------------------
if __name__ == "__main__":
    cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
        ([2, 3, 4, 5, 18, 17, 6], 17),
        ([1, 2, 4, 3], 4),
        ([0, 2], 0),
    ]
    all_ok = True
    for i, (h, expected) in enumerate(cases, 1):
        try:
            got = max_area(list(h))
            ok = got == expected
        except Exception as e:
            ok = False
            got = f"EXCEPTION: {type(e).__name__}: {e}"
        all_ok &= ok
        print(f"test {i}: {'OK ' if ok else 'FAIL'}  height={h}  attendu={expected}  got={got}")
    print("TOUS OK" if all_ok else "--> au moins un test echoue")
