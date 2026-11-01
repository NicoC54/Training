from collections import deque

def route_exists(from_row: int, from_column: int, to_row: int, to_column: int, map_matrix: list[list[bool]]) -> bool:


    if len(map_matrix) == 0 :
        return False

    number_lines = len(map_matrix)
    number_cols = len(map_matrix[0])

    if (from_row<0 or from_column <0 or from_row>=number_lines or from_column >= number_cols):
        return False

    if (to_row<0 or to_row >= number_lines or to_column<0 or to_column>= number_cols):
        return False


    visited = set()
    queue = deque()

    start_block = (from_row,from_column)
    visited.add(start_block)
    queue.append((from_row,from_column))

    while (len(queue) != 0):
        row,column = queue.popleft()


        if ((row ==to_row) and (column ==to_column) and (map_matrix[to_row][to_column] == True)):
            return True


        if ((row > 0) and (map_matrix[row-1][column] == True) and  (row-1,column) not in visited):
            queue.append((row-1,column))
            visited.add((row-1,column))

        if ((row < number_lines-1) and (map_matrix[row+1][column] == True) and  (row+1,column) not in visited):
            queue.append((row+1,column))
            visited.add((row+1,column))

        if ((column > 0) and (map_matrix[row][column-1] == True) and  (row,column-1) not in visited):
            queue.append((row,column-1))
            visited.add((row,column-1))

        if ((column < number_cols-1) and (map_matrix[row][column+1] == True) and  (row,column+1) not in visited):
            queue.append((row,column+1))
            visited.add((row,column+1))

    return False

        

        





    
 