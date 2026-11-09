"""
ex11 — Search in Rotated Sorted Array   (LeetCode medium, pattern BINARY SEARCH)

ÉNONCÉ
  On te donne un tableau `nums` d'entiers DISTINCTS, trié par ordre croissant,
  puis "tourné" (roté) à un pivot inconnu.
  Exemple de rotation : [0,1,2,4,5,6,7] roté donne [4,5,6,7,0,1,2].
  On te donne aussi une cible `target`.
  Retourne l'INDICE de `target` dans `nums`, ou -1 s'il n'y est pas.
  Objectif : O(log n) -> donc une recherche dichotomique, pas un parcours linéaire.

EXEMPLES
  nums = [4,5,6,7,0,1,2], target = 0  -> 4
  nums = [4,5,6,7,0,1,2], target = 3  -> -1
  nums = [1],             target = 0  -> -1

CONTRAINTES
  - 1 <= len(nums) <= 5000
  - toutes les valeurs sont distinctes
  - le tableau est trié-puis-roté (peut aussi ne pas être roté du tout)

IDÉE DU PATTERN
  Dichotomie classique avec left/right/mid, MAIS à chaque étape une moitié
  [left..mid] ou [mid..right] est forcément "bien triée" (croissante sans coupure).
  - Repère laquelle des deux moitiés est triée (compare nums[left] et nums[mid]).
  - Si target est DANS l'intervalle trié -> va de ce côté. Sinon -> l'autre côté.

PIÈGES DE BORNES (c'est TOUT l'enjeu de la dichotomie)
  - `while left <= right` (avec <=, sinon tu rates le dernier élément)
  - `mid = (left + right) // 2`
  - quand tu écartes une moitié : `left = mid + 1` ou `right = mid - 1` (le +1/-1 est obligatoire,
    sinon boucle infinie)
  - teste à la main un tableau de 1 et de 2 éléments

CONSIGNE DE DRILL (conditions Thalanor : solo, sans IA, sans autocomplétion)
  1. D'ABORD, écris une dichotomie SIMPLE sur un tableau trié normal (sans rotation),
     juste pour caler les bornes. Fais-la tourner dans ta tête sur [1,3,5], target=5.
  2. Ensuite ajoute la logique "quelle moitié est triée".
  3. Donne la complexité à la fin.

Écris ton code, puis lance :  python3 ex11_search_rotated.py
"""


def search(nums, target):

    left = 0
    right = len(nums)-1


    while (left <= right):
        mid =(left+right)//2

        if nums[mid] == target:    # ← LA ligne que tu as perdue
          return mid

        if nums[left] <= nums[mid]:   #range trié pivot a droite
          if nums[left] <= target <= nums[mid]:  # target a litnerieur : bingo
            right = mid-1

          else: 
              left = mid+1

        else: #range pas trié le pivot est a linterieur 
            if nums[mid] <= target <= nums[right]: # DEUX bornes aussi
              left = mid+1

            else:
              right = mid-1
            
              



    return -1


# --- tests (ne pas modifier) -------------------------------------------------
if __name__ == "__main__":
    cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([1], 1, 0),
        ([5, 1, 3], 5, 0),
        ([4, 5, 6, 7, 8, 1, 2, 3], 8, 4),
        ([1, 2, 3, 4, 5], 4, 3),      # pas roté du tout
        ([6, 7, 0, 1, 2, 4, 5], 2, 4),
        ([3, 1], 1, 1),               # 2 éléments
        ([], 5, -1),                  # tableau vide
    ]
    all_ok = True
    for i, (nums, target, expected) in enumerate(cases, 1):
        try:
            got = search(list(nums), target)
            ok = got == expected
        except Exception as e:
            ok = False
            got = f"EXCEPTION: {type(e).__name__}: {e}"
        all_ok &= ok
        print(f"test {i}: {'OK ' if ok else 'FAIL'}  nums={nums} target={target} attendu={expected} got={got}")
    print("TOUS OK" if all_ok else "--> au moins un test echoue")
