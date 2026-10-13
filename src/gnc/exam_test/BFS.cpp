#include <iostream>
#include <vector>
#include <queue>

bool routeExists(int fromRow, int fromColumn, int toRow, int toColumn,
                 const std::vector<std::vector<bool>>& mapMatrix)
{
    if (mapMatrix.empty()){
        return false;
    }
    if (fromRow < 0 || fromRow >= number_row || fromColumn < 0 || fromColumn >= number_cols) return false;
    
    // 2. On vérifie que l'arrivée est bien dans la grille
    if (toRow < 0 || toRow >= number_row || toColumn < 0 || toColumn >= number_cols) return false;

    if (mapMatrix[fromRow][fromColumn] == false || mapMatrix[toRow][toColumn] == false) return false;

    int number_row = mapMatrix.size();
    int number_cols = mapMatrix[0].size();

    if ((number_row == 0) || (number_cols == 0)){
        return false;
    }
    using Pair = std::pair<int,int>;

    std::queue<Pair> queue;
    std::vector<std::vector<bool>> visited(number_row, std::vector<bool>(number_cols,false));
    queue.push({fromRow,fromColumn});
    visited[fromRow][fromColumn] = true;

    while (!queue.empty()){
        auto [row, column] = queue.front();
        queue.pop();

        if ((row == toRow) && (column == toColumn)){
            return true;
        }

        if ((row > 0) && (mapMatrix[row-1][column] == true) && (visited[row-1][column] == false)){
            queue.push({row-1,column});
            visited[row-1][column] = true;
        }
        if ((row < number_row-1)&& (mapMatrix[row+1][column] == true) && (visited[row+1][column] == false)){
            queue.push({row+1,column});
            visited[row+1][column] = true;
        }
        if ((column > 0) && (mapMatrix[row][column-1] == true) && (visited[row][column-1] == false)){
            queue.push({row,column-1});
            visited[row][column-1] = true;
        }
        if ((column < number_cols-1) && (mapMatrix[row][column+1] == true) && (visited[row][column+1] == false)){
            queue.push({row,column+1});
            visited[row][column+1] = true;
        }  
    }

    return false;

   
}