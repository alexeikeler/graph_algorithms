def replacer(s, newstring, index, nofail=False):
    
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    if index < 0:  
        return newstring + s
    if index > len(s):  
        return s + newstring

    return s[:index] + newstring + s[index + 1:]

def find_path(n: int, r: int, c: int, given_map: list, used: list, path: list, map:list):
    
    if not used[r][c]:

        if((r + 1) < n 
        and (r + 1) >= 0 
        and (not used[r+1][c]) 
        and (given_map[r+1][c] == "." 
        or given_map[r+1][c] == "X")):
            path[r+1][c] = path[r][c] + 1
            map.insert(0, r+1)
            map.insert(0, c)
        
        if((r - 1) < n 
        and (r - 1) >= 0 
        and (not used[r-1][c]) 
        and (given_map[r-1][c] == "." 
        or given_map[r-1][c] == "X")):
        
            path[r-1][c] = path[r][c] + 1
            map.insert(0, r-1)
            map.insert(0, c)
        
        if((c + 1) < n 
        and (c + 1) >= 0 
        and (not used[r][c+1]) 
        and (given_map[r][c+1] == "." 
        or given_map[r][c+1] == "X")):
            path[r][c+1] = path[r][c] + 1
            map.insert(0, r)
            map.insert(0, c+1)
        
        if((c - 1) < n 
        and (c - 1) >= 0 
        and (not used[r][c- 1]) 
        and (given_map[r][c- 1] == "." 
        or given_map[r][c- 1] == "X")):
            path[r][c- 1] = path[r][c] + 1
            map.insert(0, r)
            map.insert(0, c - 1)
        
        used[r][c] = 1

def main():

    n = None
    x_e = None 
    y_e = None
    x = None
    y = None
    map: list = []

    n: int = int(input())
    used = [0] * n
    given_map = [0] * n
    path = [0] * n
    
    for i in range(n):
        given_map[i] = input()
        used[i] = [0] * n
        path[i] = [0] * n
        for j in range(n):
            used[i][j] = 0
            path[i][j] = -1

            if given_map[i][j] == "@":
                
                map.insert(0, i)
                map.insert(0, j)
                path[i][j] = 1
            elif given_map[i][j] == "X":
                x_e = i
                y_e = j

    while len(map) > 0:
        x = map.pop()
        y = map.pop()
        find_path(n, x, y, given_map, used, path, map)

    if not used[x_e][y_e]:
        print("N")
        return

    else:
        print("Y")
        x = x_e
        y = y_e
       
        given_map[x] = replacer(given_map[x], "+", y)
       
        while path[x][y] != 2:
            
            if ((x - 1) >= 0 and (x - 1) < n 
            and (path[x-1][y] == path[x][y] - 1)):
                x -= 1
                given_map[x] = replacer(given_map[x], "+", y)
            
            elif ((x + 1) >= 0 and (x + 1) < n 
            and (path[x+1][y] == path[x][y] - 1)):
                x += 1

                given_map[x] = replacer(given_map[x], "+", y)

            elif ((y - 1) >= 0 and (y - 1) < n 
            and (path[x][y-1] == path[x][y] - 1)):
                y -= 1

                given_map[x] = replacer(given_map[x], "+", y)
            
            elif ((y + 1) >= 0 and (y + 1) < n 
            and (path[x][y+1] == path[x][y] - 1)):
                y += 1

                given_map[x] = replacer(given_map[x], "+", y)
        
    print (*given_map, sep="\n")


if __name__ == '__main__':
    main()
