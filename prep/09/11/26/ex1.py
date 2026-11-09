"""
ex08 — Group Anagrams   (LeetCode medium classique, pattern HASHMAP)

ÉNONCÉ
  On te donne une liste de chaînes `strs`.
  Regroupe ensemble les chaînes qui sont des anagrammes les unes des autres
  (mêmes lettres, mêmes quantités, ordre différent).
  Retourne une liste de groupes (liste de listes de chaînes).
  L'ordre des groupes et l'ordre dans chaque groupe n'ont pas d'importance.

EXEMPLE
  strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
  -> [["eat","tea","ate"], ["tan","nat"], ["bat"]]

CONTRAINTES
  - 1 <= len(strs) <= 10^4
  - 0 <= len(strs[i]) <= 100
  - strs[i] ne contient que des lettres minuscules a-z
  - "" (chaîne vide) est possible et forme son propre groupe

CONSIGNE DE DRILL (conditions Thalanor : solo, sans IA, sans autocomplétion)
  1. Lis l'énoncé DEUX fois. Souligne : type de retour attendu ?
  2. Résous l'exemple À LA MAIN d'abord : quelle "clé" rend deux anagrammes égaux ?
  3. Version simple qui marche d'abord. Exécute souvent.
  4. Donne la complexité (temps) à la fin et justifie-la.

Écris ton code dans la fonction ci-dessous, puis lance :  python3 ex08_group_anagrams.py
"""


def group_anagrams(strs):

    if strs is None:
        return ""
        

    dictionnaire = {}
    list_sorted = []
    for word in strs:
        sorted_word = sorted(word)
        list_sorted.append("".join(sorted(word)))

    for i in range(len(strs)):

        if list_sorted[i] not in dictionnaire:
            dictionnaire[list_sorted[i]] = [strs[i]]

        else:
            dictionnaire[list_sorted[i]].append(strs[i])

    result = list(dictionnaire.values())

    return result

    
    pass


# --- tests (ne pas modifier) -------------------------------------------------
def _norm(groups):
    # normalise pour comparer sans tenir compte de l'ordre
    return sorted(sorted(g) for g in groups)


if __name__ == "__main__":
    cases = [
        (["eat", "tea", "tan", "ate", "nat", "bat"],
         [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["abc", "cba", "bca", "xyz"], [["abc", "bca", "cba"], ["xyz"]]),
    ]
    all_ok = True
    for i, (inp, expected) in enumerate(cases, 1):
        try:
            got = group_anagrams(inp)
            ok = _norm(got) == _norm(expected)
        except Exception as e:
            ok = False
            got = f"EXCEPTION: {e}"
        all_ok &= ok
        print(f"test {i}: {'OK ' if ok else 'FAIL'}  input={inp}  got={got}")
    print("TOUS OK" if all_ok else "--> au moins un test échoue")
