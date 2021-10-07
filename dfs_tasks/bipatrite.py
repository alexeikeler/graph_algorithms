from collections import defaultdict


def main():
    
    n, m = [int(x) for x in input().split()]
    g: Graph = Graph(n)
    
    for _ in range(m):
        
        u,v = [int(x) for x in input().split()]
        u -= 1
        v -= 1
        g.add_edge(u, v)
    
    #g.dfs(u)
    for i in range(1, n):
        if g.colors[i] == 0:
            g.colors[i] = 1
            g.dfs(i)

    if g.bipatrite:
        print("YES")
    else:
        print("NO")

class Graph:


    def __init__(self, n: int):
        self.graph = defaultdict(list)
        self.n = n
        #self.colors = [0] * n
        self.used = [1] * n
        self.bipatrite = True


    def add_edge(self, u: int, v: int) -> None:
        self.graph[u].append(v)


    def dfs(self, v: int) -> None:
        self.used[v] = 1
        for u in self.graph[v]:
            to: int = self.graph[v][u]
            temp: int = 3 - self.used[v];
            if
    
if __name__ == '__main__':
    main()