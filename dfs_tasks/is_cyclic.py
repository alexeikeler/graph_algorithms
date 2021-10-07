from collections import defaultdict


def main():
    
    n, m = [int(x) for x in input().split()]
    g: Graph = Graph(n)
    
    for _ in range(m):
        
        u,v = [int(x) for x in input().split()]
        u -= 1
        v -= 1
        g.add_edge(u, v)

    for i in range(n):
        if g.dfs(i):
            break
    
    if g.cycle_start == -1:
        print("NO")
    
    else:
        print("YES")
        print(*g.p)


    #g.dfs(u)

class Graph:


    def __init__(self, n: int):
        self.graph = defaultdict(list)
        self.n = n
        self.cl = [0] * n
        self.p = [-1] * n
        self.cycle_start = -1
        self.cycle_end = -1

    def add_edge(self, u: int, v: int) -> None:
        self.graph[u].append(v)


    def dfs(self, v: int) -> bool:
        
        self.cl[v] = 1
        for i in range(len(self.graph[v])):
            to: int = self.graph[v][i]
            if self.cl[to] == 0:
                self.p[to] = v
                if self.dfs(to):
                    return True
            elif self.cl[to] == 1:
                self.cycle_end = v
                self.cycle_start = to
                return True
        
        self.cl[v] = 2
        return False
    


    # def dfs_helper(self,v:int, visited: list) -> None:
    #     visited.add(v)
    #     for adj in self.graph[v]:
    #         if adj not in visited:
    #             self.dfs_helper(adj, visited)

    # def dfs(self, v: int) -> None:
        
    #     visited = set()
    #     self.dfs_helper(v, visited)
    #     #print(f"from {v} -> : ", visited)
    


        
        
        
        
if __name__ == '__main__':
    main()