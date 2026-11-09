"""
EXERCISE 04 - grid_path            Time limit: 30 min          No AI, no internet

Routine: read twice -> solve the example by hand -> plan out loud -> SIMPLE version first
-> run every 5 min -> tick every requirement before handing in.

Context
-------
A ground robot moves on an occupancy grid:

    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0],
    ]
    0 = free cell, 1 = obstacle. A cell is (row, col), (0, 0) is top left.
    The robot moves 4-connected: up, down, left, right (no diagonals). Each move costs 1.

Part A - shortest_path_length(grid, start, goal)                     (~15 min)
-----------------------------------------------
Return the MINIMUM number of moves from start to goal, or -1 if goal is unreachable.
Use BFS (breadth-first search) with a queue: from collections import deque.
  - start == goal -> 0
  - start or goal on an obstacle -> -1

    shortest_path_length(grid, (0, 0), (3, 3))  ->  6
    shortest_path_length(grid, (0, 0), (3, 0))  ->  7

Part B - shortest_path(grid, start, goal)                             (~10 min)
----------------------------------------
Same search, but return the list of cells of one shortest path, from start to goal
included, or [] if unreachable. Hint: remember for each cell the cell you came from
(a `parent` dict), then walk back from goal to start.

    len(shortest_path(grid, (0, 0), (3, 3)))  ->  7    (6 moves = 7 cells)

Constraints
-----------
  - At least 4 tests with `assert`: the examples, start == goal, an unreachable goal.
  - In a comment at the end:
        * the complexity of BFS on an R x C grid;
        * why BFS gives the shortest path here, and what you would use instead
          if moves had different costs (e.g. diagonals cost 1.41).

Paste your code AND the terminal output in the chat, with the time taken.
"""
from collections import deque

def shortest_path_length(grid, start, goal):

    max_cols = len(grid[0])
    max_lines = len (grid)

    if (grid is None) or (start[1] > max_cols-1) or (start[0] > max_lines-1) or (grid[start[0]][start[1]] == 1) :
        return -1

    if start[0] < 0 or start[1] < 0 :
        return -1
    
    if (goal[1] > max_cols-1) or (goal[0] > max_lines-1) or (grid[goal[0]][goal[1]] == 1) :
        return -1

    if goal[0] < 0 or goal[1] < 0 :
        return -1

    visited = set()
    start_line = start[0]
    start_col =  start[1]
    distances = {}
    distances[start]=0

    visited.add((start_line,start_col))

    queue = deque([start]) 

    while len(queue)!=0:

         actual_node = queue.popleft()

         c = actual_node[1]
         r = actual_node[0]

         visited.add((r,c))

         if actual_node == goal:
            return distances[actual_node[0],actual_node[1]]

         if (r < max_lines - 1) and (grid[r+1][c] !=1 and ((r+1,c) not in visited)) :
            queue.append((r+1,c))
            visited.add((r+1,c))
            distances[(r+1,c)] = distances[actual_node]+1

         if r > 0  and (grid[r-1][c] !=1 and ((r-1,c) not in visited)) :
            queue.append((r-1,c))
            visited.add((r-1,c))
            distances[(r-1,c)] = distances[actual_node]+1

         if (c < max_cols - 1) and (grid[r][c+1] !=1 and ((r,c+1) not in visited)):
            queue.append((r,c+1))
            visited.add((r,c+1))
            distances[(r,c+1)] = distances[actual_node]+1

         if (c > 0) and (grid[r][c-1] !=1 and ((r,c-1) not in visited)):
            queue.append((r,c-1))
            visited.add((r,c-1))
            distances[(r,c-1)] = distances[actual_node]+1



    return -1
              


def shortest_path(grid, start, goal):

    max_cols = len(grid[0])
    max_lines = len (grid)

    if (grid is None) or (start[1] > max_cols-1) or (start[0] > max_lines-1) or (grid[start[0]][start[1]] == 1) :
        return -1

    if start[0] < 0 or start[1] < 0 :
        return -1
    
    if (goal[1] > max_cols-1) or (goal[0] > max_lines-1) or (grid[goal[0]][goal[1]] == 1) :
        return -1

    if goal[0] < 0 or goal[1] < 0 :
        return -1

    visited = set()
    start_line = start[0]
    start_col =  start[1]
    parents = {}
    parents[start]=None

    visited.add((start_line,start_col))

    queue = deque([start]) 

    while len(queue)!=0:

         actual_node = queue.popleft()

         c = actual_node[1]
         r = actual_node[0]

         visited.add((r,c))

         if actual_node == goal:
            path = []
            parent = parents[actual_node]
            path.append(parent)
            while parent != None:
                parent = parents[parent]
                path.append(parent)
            correct_path = path[::-1]
            return correct_path


         if (r < max_lines - 1) and (grid[r+1][c] !=1 and ((r+1,c) not in visited)) :
            queue.append((r+1,c))
            visited.add((r+1,c))
            parents[(r+1,c)] = actual_node

         if r > 0  and (grid[r-1][c] !=1 and ((r-1,c) not in visited)) :
            queue.append((r-1,c))
            visited.add((r-1,c))
            parents[(r-1,c)] = actual_node

         if (c < max_cols - 1) and (grid[r][c+1] !=1 and ((r,c+1) not in visited)):
            queue.append((r,c+1))
            visited.add((r,c+1))
            parents[(r,c+1)] = actual_node

         if (c > 0) and (grid[r][c-1] !=1 and ((r,c-1) not in visited)):
            queue.append((r,c-1))
            visited.add((r,c-1))
            parents[(r,c-1)] = actual_node



    return -1


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0],
    ]
    # TODO: your tests
    pass
