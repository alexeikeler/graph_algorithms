global n, index, start, end
n = 0
index = 0
desk: list = [None]
temp_desk:list = [None]
inpt: bool = False
lst: list = []
start = (0, 0)
end = (0, 0)

def move(x: str, y: str, k: int) -> None:
    if 0 <= x and x < n and 0 <= y and y < n:
        if temp_desk[x][y] != "#":
            temp_desk[x][y] = "#"
            lst.append(((x,y),k))


def main():
    global index, start, end, inpt, n, desk, temp_desk
    x_s = None
    y_s = None
    n = int(input())
    desk = [None] * n
    temp_desk = [None] * n


    for i in range(n):
        row = input()
        temp_desk[i] = [None]*n
        desk[i] = [None] * n
        for j in range(n):
            if row[j] == "@" and not inpt:
                start = (i, j)
                inpt = True
            elif row[j] == "@":
                end = (i, j)
            
            desk[i][j] = row[j]
            temp_desk[i][j] = row[j]
    
    move(start[0], start[1], 0)

    while lst[index][0] != end:
        x_s = lst[index][0][0]
        y_s = lst[index][0][1]

        move(x_s+1, y_s+2, index)

        move(x_s +2, y_s+1, index)

        move(x_s-1, y_s+2, index)

        move(x_s+2, y_s-1, index)

        move(x_s+1, y_s-2, index)

        move(x_s-2, y_s+1, index)

        move(x_s-1, y_s-2, index)

        move(x_s-2, y_s-1, index)

        index += 1

        if index >= len(lst):
            print("Impossible")
            return
    
    while index != 0:
        desk[lst[index][0][0]][lst[index][0][1]] = "@"
        index = lst[index][1]
    
    
    for layer in desk:
        print(*layer, sep="", end= "")
        print()

if __name__ == '__main__':
    main()


