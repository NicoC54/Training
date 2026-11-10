"""
ex16 — RÉVISION : Search in Rotated Sorted Array   (pattern BINARY SEARCH)

/!\\ À FROID. Ne regarde PAS ex11. Conditions Thalanor : seul, sans IA, sans autocomplétion.

ÉNONCÉ
  Tableau `nums` d'entiers DISTINCTS, trié croissant puis "roté" à un pivot inconnu.
  Ex : [0,1,2,4,5,6,7] roté -> [4,5,6,7,0,1,2].
  On te donne `target`. Retourne son INDICE, ou -1 s'il n'y est pas.
  Objectif : O(log n) -> dichotomie, pas de parcours linéaire.

EXEMPLES
  nums=[4,5,6,7,0,1,2], target=0  -> 4
  nums=[4,5,6,7,0,1,2], target=3  -> -1
  nums=[1],             target=0  -> -1

MÉTHODE (rappelle-la toi AVANT de coder, dans ta tête) :
  1. dichotomie : left, right, mid = (left+right)//2, while left <= right
  2. une moitié est TOUJOURS triée -> repère laquelle (nums[left] vs nums[mid])
  3. target est-il DANS la moitié triée (les 2 bornes) ? oui -> va dedans, non -> l'autre côté

Écris ton code, puis lance :  python3 ex16_rev_search_rotated.py
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
        ([5, 1, 2, 3, 4], 1, 1),
        ([7, 8, 1, 2, 3, 4, 5, 6], 6, 7),
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
