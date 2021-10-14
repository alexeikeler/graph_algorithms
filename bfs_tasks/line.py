from typing import List

global i, j, n, matrix


class Cell:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y


q: List[Cell] = []

def CanGo(i: int, j: int) -> int:
    global n
    if i < 0 or i >= n or j < 0 or j >= n:
        return 0
    if matrix[i][j] != 1:
        return 0
    return 1

def bfs(start: Cell) -> None:
    print(f"\nbfs enter in point {start.x} {start.y}")
    i = start.x
    j = start.y

    dx: List[int] = [1, -1, 0, 0]
    dy: List[int] = [0, 0, 1, -1]

    q.insert(0, start)
    matrix[i][j] = 0
    
    while len(q) > 0:
        
        i = q.pop().x
        j = q.pop().y

        if i == finish.x and j == finish.y:
            return
        
        for k in range(4):
            
            ii: int = i + dx[k]
            jj: int = j + dy[k]

            if CanGo(ii, jj):
                
                q.insert(Cell(ii, jj))
                matrix[ii][jj] = matrix[i][j] + 1

def main():
    
    global n, start, finish, i, j, matrix
    
    n = int(input())
    matrix = [-1]*n

    for i in range(n):
        row = input()
        for j in range(n):
            if row[j] == "@":
                print(f"start set to {i} {j}")
                start = Cell(i, j)
            if row[j] == "X":
                print(f"end set to {i} {j}")
                finish = Cell(i, j)
            elif row[j] == "O":
                matrix[i] = [-1] * n
                matrix[i][j] = -2

    bfs(start)

    if matrix[finish.x][finish.y] == -1:
        print("N")
        return
    
    print("Y")
    
    i = finish.x
    j = finish.y

    cnt: int = matrix[finish.x][finish.y]

    for k in range(cnt):

        ii: int = i
        jj: int = j

        if i > 0 and matrix[i - 1][j] == matrix[i][j] - 1:
            i -= 1
        else:
            if i < n-1 and matrix[i+1][j] == matrix[i][j] -1:
                i += 1
            else:
                if j > 0 and matrix[i][j-1] == matrix[i][j] -1:
                    j -= 1
                else:
                    if j < n and matrix[i][j+1] == matrix[i][j] - 1:
                        j += 1
        
        matrix[ii][jj] = -3
    
    for i in range(n):
        for j in range(n):
            c: str = "."
            if matrix[i][j] == -2:
                c = "O"
            if matrix[i][j] == 0:
                c = "@"
            if matrix[i][j] == -3:
                c = "+"
            print(f"{c} ")
        print()


if __name__ == '__main__':
    main()





        