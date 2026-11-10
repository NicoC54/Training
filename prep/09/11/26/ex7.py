"""
ex14 — Valid Parentheses   (pattern STACK / pile)

ÉNONCÉ
  On te donne une chaîne `s` composée uniquement des caractères : ( ) { } [ ]
  Dis si la chaîne est VALIDE. Elle est valide si :
    - chaque parenthèse ouvrante est fermée par la MÊME sorte de fermante,
    - les parenthèses sont fermées dans le BON ORDRE,
    - toute fermante a une ouvrante correspondante.
  Retourne True ou False (un booléen).

EXEMPLES
  "()"        -> True
  "()[]{}"    -> True
  "(]"        -> False   (mauvais appariement)
  "([)]"      -> False   (mauvais ordre)
  "{[]}"      -> True    (imbrication correcte)
  "("         -> False   (jamais fermée)
  ""          -> True    (vide = valide)

CONTRAINTES
  - 0 <= len(s) <= 10^4
  - s ne contient que ( ) { } [ ]

IDÉE DU PATTERN (stack / pile)
  - Une pile (une simple liste Python : .append pour empiler, .pop pour dépiler).
  - Parcours les caractères :
      - ouvrante  ( [ {  -> on l'EMPILE
      - fermante  ) ] }  -> on regarde le SOMMET de la pile :
            * si la pile est vide -> rien à fermer -> False
            * si le sommet n'est pas l'ouvrante correspondante -> False
            * sinon -> on DÉPILE (la paire est consommée)
  - À la fin : la chaîne est valide SEULEMENT si la pile est VIDE
    (sinon il reste des ouvrantes jamais fermées).

ASTUCE : un dico qui associe chaque fermante à son ouvrante
  paires = {')': '(', ']': '[', '}': '{'}

CONSIGNE DE DRILL (conditions Thalanor : solo, sans IA, sans autocomplétion)
  1. Lis l'énoncé DEUX fois. Type de retour ? (booléen)
  2. Déroule À LA MAIN "([)]" : pourquoi False ? et "{[]}" : pourquoi True ?
  3. N'oublie pas le test final "pile vide ?".
  4. Donne la complexité à la fin.

Écris ton code, puis lance :  python3 ex14_valid_parentheses.py
"""

from collections import deque


def is_valid(s):

    stack = deque()

    for letter in s:

        if (letter == "[") or (letter == "(") or (letter == "{"):
            stack.append(letter)

        elif (letter == "]"):
            if not stack:
                return False
            top_stack = stack.pop()
            if top_stack != "[":
                return False

        elif (letter == ")"):
                    if not stack:
                        return False
                    top_stack = stack.pop()
                    if top_stack != "(":
                        return False

        elif (letter == "}"):
                    if not stack:
                        return False
                    top_stack = stack.pop()
                    if top_stack != "{":
                        return False
                    
    if not stack:
         return True

    return False

    


    



# --- tests (ne pas modifier) -------------------------------------------------
if __name__ == "__main__":
    cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("(", False),
        (")", False),
        ("", True),
        ("((", False),
        ("){", False),
        ("([{}])", True),
    ]
    all_ok = True
    for i, (s, expected) in enumerate(cases, 1):
        try:
            got = is_valid(s)
            ok = got == expected
        except Exception as e:
            ok = False
            got = f"EXCEPTION: {type(e).__name__}: {e}"
        all_ok &= ok
        print(f"test {i}: {'OK ' if ok else 'FAIL'}  s={s!r:10} attendu={expected}  got={got}")
    print("TOUS OK" if all_ok else "--> au moins un test echoue")
