
def main():
    m, n = [int(x) for x in input().split()]
    g = [["#" for x in range(n)] for y in range(m)]
    counter = 1

    for i in range(m):
        row = input()
        for j in range(len(row)):
            g[i][j] = row[j]
    
    components = [[0 for x in range(n)] for y in range(m)]

    for i in range(m):
        for j in range(n):
            if bfs(i, j, g, components, counter):
                counter += 1
    
    print(counter - 1)


def bfs(m: int, n: int, g: list, components: list, counter: int) -> bool:

    if m < 0 or m >= len(g):
        return False
    
    if n < 0 or n >= len(g[0]):
        return False
    
    if g[m][n] == ".":
        return False
    
    if components[m][n] != 0:
        return False
    
    components[m][n] = counter

    bfs(m - 1, n, g, components, counter)
    bfs(m + 1, n, g, components, counter)
    bfs(m, n - 1, g, components, counter)
    bfs(m, n + 1, g, components, counter)

    return True

if __name__ == "__main__":
    main()