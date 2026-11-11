"""
MOCK 2 — conditions reelles (chrono 20 min, seul, sans IA, sans autocompletion)
À toi de reconnaitre le pattern. Parle a voix haute, donne la complexite a la fin.

ÉNONCÉ
  Tu montes un escalier de `n` marches.
  À chaque pas, tu peux monter SOIT 1 marche, SOIT 2 marches.
  De combien de FAÇONS DIFFERENTES peux-tu arriver exactement en haut (marche n) ?
  Retourne un entier (le nombre de facons).

EXEMPLES
  n = 2  -> 2    (1+1  ou  2)
  n = 3  -> 3    (1+1+1 , 1+2 , 2+1)
  n = 4  -> 5    (1+1+1+1 , 1+1+2 , 1+2+1 , 2+1+1 , 2+2)

CONTRAINTES
  - 1 <= n <= 45
  - (n = 0 : on considere qu'il y a 1 facon : ne pas bouger)

INDICE (les 3 questions DP, a te poser toi-meme)
  1. "Mon record jusqu'a la marche i ?"  -> ways[i] = nb de facons d'atteindre la marche i
  2. "Pour atteindre la marche i, d'ou je viens ?"  -> de la marche i-1 (pas de 1) OU de i-2 (pas de 2)
  3. "Donc ways[i] = ... ?"  (combine les deux provenances)
  Puis : version 2 variables (O(1) espace), comme House Robber.

Écris ta fonction climb_stairs(n), puis lance :
    python3 mock2_climbing_stairs.py
"""


def climb_stairs(n):

    if n==0:
        return 1

    possibilities_table = [0] * (n+1)
    possibilities_table[0] = 1
    possibilities_table[1] = 1

    for i in range(2,n+1):

        possibilities_table[i] = possibilities_table[i-1] + possibilities_table[i-2]


    return possibilities_table[n]



      

    


    



    
    pass


# --- tests (ne pas modifier) -------------------------------------------------
if __name__ == "__main__":
    cases = [
        (2, 2), (3, 3), (4, 5), (1, 1), (5, 8),
        (10, 89), (0, 1), (20, 10946), (45, 1836311903),
    ]
    all_ok = True
    for i, (n, expected) in enumerate(cases, 1):
        try:
            got = climb_stairs(n)
            ok = got == expected
        except Exception as e:
            ok = False
            got = f"EXCEPTION: {type(e).__name__}: {e}"
        all_ok &= ok
        print(f"test {i}: {'OK ' if ok else 'FAIL'}  n={n}  attendu={expected}  got={got}")
    print("TOUS OK" if all_ok else "--> au moins un test echoue")
