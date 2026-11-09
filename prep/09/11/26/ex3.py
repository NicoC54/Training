"""
ex10 — Number of Islands   (LeetCode medium, pattern BFS/DFS sur grille)

ÉNONCÉ
  On te donne une grille 2D `grid` de caractères '1' (terre) et '0' (eau).
  Compte le nombre d'ÎLOTS.
  Un îlot = un groupe de cases '1' connectées horizontalement ou verticalement
  (PAS en diagonale). Les bords de la grille sont entourés d'eau.
  Retourne un entier.

EXEMPLE
  grid = [
    ['1','1','0','0','0'],
    ['1','1','0','0','0'],
    ['0','0','1','0','0'],
    ['0','0','0','1','1'],
  ]
  -> 3   (le bloc en haut-gauche, la case du milieu, le bloc en bas-droite)

CONTRAINTES
  - 1 <= rows, cols <= 300
  - grid[r][c] vaut '1' ou '0' (des CHAÎNES, pas des entiers)

IDÉE DU PATTERN (flood fill)
  - Parcours chaque case de la grille.
  - Quand tu tombes sur un '1' pas encore visité : c'est un NOUVEL îlot -> compteur += 1,
    puis tu "noies" tout l'îlot connecté (BFS ou DFS) pour ne pas le recompter.
  - "Noyer" = marquer chaque '1' de l'îlot comme visité (ex. le passer à '0',
    ou utiliser un set `visited`).
  - Voisins = haut, bas, gauche, droite (4 directions).

CONSIGNE DE DRILL (conditions Thalanor : solo, sans IA, sans autocomplétion)
  1. Lis l'énoncé DEUX fois. Type de retour ? (un entier)
  2. Grille : `rows = len(grid)`, `cols = len(grid[0])`. Teste une grille NON carrée.
  3. Voisins : garde les 4 bornes (0 <= nr < rows ET 0 <= nc < cols) avant d'y toucher.
  4. Version simple qui marche d'abord. Donne la complexité à la fin.

ASTUCE voisins (pour éviter 4 blocs if) :
  for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
      nr, nc = r + dr, c + dc

Écris ton code, puis lance :  python3 ex10_number_of_islands.py
"""

from collections import deque


def num_islands(grid):

    if grid is None:
        return 0


    visited = set()
    number_lines = len(grid)
    number_cols = len(grid[0])
    number_islands = 0

    previous_node_value = 0

    queue = deque()

    queue.append((0,0))

    while len(queue)!=0:

        current_line,current_col = queue.popleft()

        current_node_value = grid[current_line][current_col] 

        if previous_node_value == 0 and current_node_value == 1:
            number_islands+=1


        if current_line > 0 and (current_line-1, current_col) not in visited :
            queue.append((current_line-1, current_col))
            visited.add((current_line-1, current_col))
            previous_node_value = current_node_value
        
        if current_line < number_lines-1 and (current_line+1, current_col) not in visited:
            queue.append((current_line+1, current_col))
            visited.add((current_line+1, current_col))
            previous_node_value = current_node_value


        if current_col > 0 and (current_line, current_col-1) not in visited :
            queue.append((current_line, current_col-1))
            visited.add((current_line, current_col-1))
            previous_node_value = current_node_value

        if current_col < number_cols-1 and (current_line, current_col+1) not in visited :
            queue.append((current_line, current_col+1))
            visited.add((current_line, current_col+1))
            previous_node_value = current_node_value


    return number_islands
        

       

        
            





    

# --- tests (ne pas modifier) -------------------------------------------------
if __name__ == "__main__":
    def g(rows):  # transforme des chaînes "110" en [['1','1','0'], ...]
        return [list(r) for r in rows]

    cases = [
        (g(["11000", "11000", "00100", "00011"]), 3),
        (g(["111", "010", "111"]), 1),
        (g(["000", "000"]), 0),
        (g(["1"]), 1),
        (g(["0"]), 0),
        (g(["101", "010", "101"]), 5),   # damier : 5 îlots d'une case
        (g(["1100", "0110", "0011"]), 1), # diagonale connectée par les coins -> 1 seul (touche H/V)
    ]
    all_ok = True
    for i, (grid, expected) in enumerate(cases, 1):
        # on copie la grille car la solution peut la modifier
        import copy
        got_input = copy.deepcopy(grid)
        try:
            got = num_islands(got_input)
            ok = got == expected
        except Exception as e:
            ok = False
            got = f"EXCEPTION: {type(e).__name__}: {e}"
        all_ok &= ok
        print(f"test {i}: {'OK ' if ok else 'FAIL'}  attendu={expected}  got={got}")
    print("TOUS OK" if all_ok else "--> au moins un test echoue")
