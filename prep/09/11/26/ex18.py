"""
MOCK 1 — conditions reelles (chrono 25 min, seul, sans IA, sans autocompletion)
À toi de reconnaitre le pattern. Parle a voix haute, donne la complexite a la fin.

ÉNONCÉ
  On te donne une liste d'entiers `nums` et un entier `k`.
  Retourne les `k` elements qui apparaissent le PLUS souvent dans `nums`.
  La reponse peut etre dans n'importe quel ordre.
  Tu peux supposer que la reponse est unique (pas d'egalite ambigue sur le k-eme).

EXEMPLES
  nums = [1,1,1,2,2,3], k = 2   -> [1,2]   (1 apparait 3x, 2 apparait 2x)
  nums = [1],          k = 1    -> [1]
  nums = [4,4,4,5,5,6], k = 1   -> [4]

CONTRAINTES
  - 1 <= len(nums) <= 10^5
  - k est valide : 1 <= k <= nombre de valeurs distinctes
  - les valeurs peuvent etre negatives

Écris ta fonction top_k_frequent(nums, k), puis lance :
    python3 mock1_top_k_frequent.py
"""


def top_k_frequent(nums, k):

    dictionnary = {}
    results=[]

    for number in nums:

        if number not in dictionnary:
            dictionnary[number]=1
        else:
            dictionnary[number]+=1

    items_list = list(dictionnary.items())


    sorted_by_apparition = sorted(items_list, key = lambda k : k[1], reverse = True)

    for i in range(k):
        results.append(sorted_by_apparition[i][0])


    return results

    


# --- tests (ne pas modifier) -------------------------------------------------
if __name__ == "__main__":
    def norm(res):
        return sorted(res)

    cases = [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        ([4, 4, 4, 5, 5, 6], 1, [4]),
        ([-1, -1, -2, -2, -2, 3], 2, [-2, -1]),
        ([5, 5, 5, 5], 1, [5]),
        ([1, 2, 3, 4, 5, 5, 4, 3, 5, 4], 2, [4, 5]),
        ([7, 7, 8, 8, 9], 3, [7, 8, 9]),
    ]
    all_ok = True
    for i, (nums, k, expected) in enumerate(cases, 1):
        try:
            got = top_k_frequent(list(nums), k)
            ok = norm(got) == norm(expected)
        except Exception as e:
            ok = False
            got = f"EXCEPTION: {type(e).__name__}: {e}"
        all_ok &= ok
        print(f"test {i}: {'OK ' if ok else 'FAIL'}  nums={nums} k={k} attendu={expected} got={got}")
    print("TOUS OK" if all_ok else "--> au moins un test echoue")
