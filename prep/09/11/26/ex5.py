"""
ex12 — Merge Intervals   (LeetCode medium, pattern INTERVALLES / tri)

ÉNONCÉ
  On te donne une liste d'intervalles `intervals`, chacun étant [début, fin].
  Fusionne tous les intervalles qui se CHEVAUCHENT, et retourne la liste des
  intervalles résultants (qui ne se chevauchent plus).
  Deux intervalles se chevauchent s'ils se touchent ou se recouvrent.

EXEMPLES
  [[1,3],[2,6],[8,10],[15,18]] -> [[1,6],[8,10],[15,18]]
      ([1,3] et [2,6] se chevauchent -> [1,6])
  [[1,4],[4,5]] -> [[1,5]]
      (ils se touchent en 4 -> on fusionne)

CONTRAINTES
  - 1 <= len(intervals) <= 10^4
  - intervals[i] = [debut_i, fin_i] avec debut_i <= fin_i
  - les intervalles sont donnés dans un ORDRE QUELCONQUE (pas triés !)

IDÉE DU PATTERN
  1. TRIER les intervalles par leur DÉBUT. (c'est l'étape clé : sans tri, impossible)
  2. Parcourir dans l'ordre. Garder une liste `result`.
     Pour chaque intervalle courant :
       - s'il chevauche le DERNIER intervalle de `result`
         (son début <= fin du dernier) -> on ÉTEND ce dernier
         (sa fin = max(fin du dernier, fin du courant))
       - sinon -> on AJOUTE le courant comme nouvel intervalle dans `result`

PIÈGES
  - bien trier par le DÉBUT : `intervals.sort(key=lambda x: x[0])`
  - "chevauche" inclut "se touche" -> `<=` (pas `<`)
  - étendre avec `max(...)` : [1,9] et [2,5] fusionnés donnent [1,9], pas [1,5]
  - le premier intervalle : initialise `result` avec lui, puis boucle sur le reste
    (ou result=[] et un cas spécial quand result est vide)

CONSIGNE DE DRILL (conditions Thalanor : solo, sans IA, sans autocomplétion)
  1. Lis l'énoncé DEUX fois. Type de retour ? (liste de listes [début, fin])
  2. Déroule À LA MAIN [[1,3],[2,6],[8,10]] : quand on étend, quand on ajoute ?
  3. Trie d'abord. Exécute souvent. Donne la complexité à la fin.

Écris ton code, puis lance :  python3 ex12_merge_intervals.py
"""


def merge(intervals):

    if intervals is None:
        return []

    sort_list = sorted(intervals, key = lambda k:k[0])
    result_intervals = []

    for i in range (len(sort_list)):

        if i ==0:

            new_entrance = sort_list[i][0]
            new_ending = sort_list[i][1]
            result_intervals.append([new_entrance,new_ending])
            last_ending = new_ending

        if i >= 1 :

            new_entrance = sort_list[i][0]
            new_ending = sort_list[i][1]

        if new_entrance > last_ending:
            last_ending = new_ending
            result_intervals.append([new_entrance,new_ending])
            

        elif (new_entrance < last_ending) and (new_ending > last_ending):
            last_ending = new_ending
            result_intervals[-1][1]=new_ending

        elif new_entrance == last_ending :
            last_ending = new_ending
            result_intervals[-1][1]=new_ending


    return result_intervals


















    
  


# --- tests (ne pas modifier) -------------------------------------------------
if __name__ == "__main__":
    def norm(res):
        return sorted([list(x) for x in res])

    cases = [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),                       # se touchent
        ([[1, 4], [2, 3]], [[1, 4]]),                       # un inclus dans l'autre
        ([[1, 4], [5, 6]], [[1, 4], [5, 6]]),               # pas de chevauchement
        ([[1, 4]], [[1, 4]]),                               # un seul
        ([[2, 3], [1, 5]], [[1, 5]]),                       # pas triés au depart
        ([[1, 9], [2, 5], [3, 4]], [[1, 9]]),               # tout inclus dans le 1er
        ([[1, 4], [0, 2], [3, 5]], [[0, 5]]),               # fusion en chaine
    ]
    all_ok = True
    for i, (inp, expected) in enumerate(cases, 1):
        import copy
        try:
            got = merge(copy.deepcopy(inp))
            ok = norm(got) == norm(expected)
        except Exception as e:
            ok = False
            got = f"EXCEPTION: {type(e).__name__}: {e}"
        all_ok &= ok
        print(f"test {i}: {'OK ' if ok else 'FAIL'}  in={inp}  attendu={expected}  got={got}")
    print("TOUS OK" if all_ok else "--> au moins un test echoue")
