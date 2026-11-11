"""
ex15 — House Robber   (LeetCode medium, pattern DP simple / programmation dynamique)

ÉNONCÉ
  Des maisons alignées, chacune avec un montant d'argent : `nums[i]`.
  Tu es un cambrioleur, mais tu ne peux PAS cambrioler deux maisons ADJACENTES
  (l'alarme se déclenche). Quel est le montant MAXIMAL que tu peux voler ?
  Retourne un entier.

EXEMPLES
  [1,2,3,1]     -> 4   (maison 0 + maison 2 = 1+3 = 4)
  [2,7,9,3,1]   -> 12  (maison 0 + 2 + 4 = 2+9+1 = 12)
  [5]           -> 5
  [2,1,1,2]     -> 4   (maison 0 + maison 3 = 2+2 = 4)

CONTRAINTES
  - 0 <= len(nums) <= 100
  - 0 <= nums[i]

IDÉE DU PATTERN (DP : on résout maison par maison)
  À chaque maison i, tu as DEUX choix :
    - NE PAS la cambrioler -> tu gardes le meilleur total obtenu jusqu'à i-1
    - LA cambrioler        -> nums[i] + le meilleur total jusqu'à i-2
                              (i-2 parce que i-1 est interdite, adjacente)
  Le meilleur à la maison i = max(de ces deux choix).

  Formule (la "récurrence") :
      best[i] = max(best[i-1],  nums[i] + best[i-2])

  Astuce : pas besoin d'un tableau complet. Tu n'as besoin que des DEUX derniers
  totaux. Garde deux variables :
      prev1 = meilleur jusqu'à i-1
      prev2 = meilleur jusqu'à i-2
  et fais-les glisser à chaque étape.

CONSIGNE DE DRILL (conditions Thalanor : solo, sans IA, sans autocomplétion)
  1. Lis l'énoncé DEUX fois. Type de retour ? (un entier)
  2. Gère les cas de bord : liste vide -> 0 ; un seul élément -> cet élément.
  3. Déroule À LA MAIN [2,7,9,3,1] : écris prev2, prev1 à chaque étape.
  4. Version "deux variables" (O(1) espace). Donne la complexité.

Écris ton code, puis lance :  python3 ex15_house_robber.py
"""


def rob(nums):

    prev_score = 0
    prev_prev_score = 0
    total_score = 0

    for i in range(len(nums)):

        total_score = max(prev_prev_score + nums[i], prev_score)

        prev_prev_score = prev_score
        prev_score = total_score

    return total_score










# --- tests (ne pas modifier) -------------------------------------------------
if __name__ == "__main__":
    cases = [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([5], 5),
        ([2, 1, 1, 2], 4),
        ([], 0),
        ([0], 0),
        ([2, 1], 2),
        ([1, 2], 2),
        ([100, 1, 1, 100], 200),
        ([5, 5, 10, 100, 10, 5], 110),
    ]
    all_ok = True
    for i, (nums, expected) in enumerate(cases, 1):
        try:
            got = rob(list(nums))
            ok = got == expected
        except Exception as e:
            ok = False
            got = f"EXCEPTION: {type(e).__name__}: {e}"
        all_ok &= ok
        print(f"test {i}: {'OK ' if ok else 'FAIL'}  nums={nums}  attendu={expected}  got={got}")
    print("TOUS OK" if all_ok else "--> au moins un test echoue")
