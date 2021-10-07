import enum
from collections import deque
colors = []
g = []
stack = deque()
found = False
end = -1


WHITE = 0
GREY = 1
BLACK = 2


def main():
    global colors, g, end, stack, found
    n, m = [int(x) for x in input().split()]
    
    g = [[] for _ in range(n+1)]
    colors = [WHITE] * (n + 1)

    temp: int = -1
    result: list = []

    for _ in range(m):
        u, v = [int(x) for x in input().split()]
        g[u].append(v)
    
    for i in range(1, n+1):
        dfs(i)
        if found:
            break
    
    while True:
        if len(stack) == 0:
            break

        temp = stack.popleft()
        result.append(temp)

        if temp == end:
            break
    
    result = result[::-1]

    if found:
        print("YES")
        print(*result)
    else:
        print("NO")


def dfs(v: int) -> None:
    global colors, g, end, stack, found

    if found:
        return
    
    if colors[v] == BLACK:
        return
    
    colors[v] = GREY

    stack.appendleft(v)

    for x in g[v]:

        if found:
            return

        if colors[x] == WHITE:
            dfs(x)
        
        if colors[x] == GREY:
            if not found:
                end = x
                found = True
            return
    
    colors[v] = BLACK
    stack.popleft()

if __name__ == "__main__":
    main()