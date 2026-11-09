"""
ex09 — Longest Substring Without Repeating Characters
        (LeetCode medium "coeur", pattern SLIDING WINDOW)

ÉNONCÉ
  On te donne une chaîne `s`.
  Trouve la LONGUEUR de la plus longue sous-chaîne (contiguë) qui ne contient
  AUCUN caractère répété.
  Retourne un entier.

EXEMPLES
  s = "abcabcbb" -> 3   ("abc")
  s = "bbbbb"    -> 1   ("b")
  s = "pwwkew"   -> 3   ("wke" ; attention : "pwke" n'est PAS contigu)
  s = ""         -> 0

CONTRAINTES
  - 0 <= len(s) <= 5*10^4
  - s contient des lettres, chiffres, symboles, espaces

IDÉE DU PATTERN (sliding window)
  - Deux indices `left` et `right` délimitent une fenêtre [left, right].
  - `right` avance d'un cran à chaque tour (il lit un nouveau caractère).
  - Si ce caractère crée un doublon DANS la fenêtre, on fait avancer `left`
    jusqu'à ce que la fenêtre redevienne valide (sans doublon).
  - À chaque tour, la taille de la fenêtre valide = right - left + 1 ;
    on garde le maximum.
  - Un `set` (ou un dict) dit en O(1) si un caractère est déjà dans la fenêtre.

CONSIGNE DE DRILL (conditions Thalanor : solo, sans IA, sans autocomplétion)
  1. Lis l'énoncé DEUX fois. Type de retour ? (un entier)
  2. Déroule "pwwkew" À LA MAIN : où est `left`, où est `right`, quand recule la fenêtre ?
  3. Version simple qui marche d'abord. Exécute souvent.
  4. Donne la complexité (temps) à la fin et justifie-la.

Écris ton code, puis lance :  python3 ex09_longest_unique_substring.py
"""

from collections import deque

def length_of_longest_substring(s):

    liste_carac = deque()
    length = len(liste_carac)
    max_length = 0


    for char in s:

        if char in s:
            while char in liste_carac:
                liste_carac.popleft()
            liste_carac.append(char)

        else:
            liste_carac.append(char)


        length = len(liste_carac)

        if length > max_length:
            max_length = length



    return max_length
            



    


# --- tests (ne pas modifier) -------------------------------------------------
if __name__ == "__main__":
    cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("a", 1),
        ("au", 2),
        ("dvdf", 3),          # piège : "vdf" (left doit sauter au bon endroit)
        ("abba", 2),          # piège classique : left ne doit jamais reculer
        (" ", 1),
        ("tmmzuxt", 5),       # "mzuxt"
    ]
    all_ok = True
    for i, (inp, expected) in enumerate(cases, 1):
        try:
            got = length_of_longest_substring(inp)
            ok = got == expected
        except Exception as e:
            ok = False
            got = f"EXCEPTION: {type(e).__name__}: {e}"
        all_ok &= ok
        print(f"test {i}: {'OK ' if ok else 'FAIL'}  s={inp!r:12} attendu={expected}  got={got}")
    print("TOUS OK" if all_ok else "--> au moins un test echoue")
