from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        #self.graph_as_matrix = adj_matrix
    
    def add_edge(self, u: int, v: int) -> None:
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def bfs(self, start: int) -> None:

        visited:list = [False] * (max(self.graph) + 1)
        queue: list = []
        
        queue.append(start)
        visited[start] = True

        while queue:
            start = queue.pop(0)
            print(start, end = " ")
            
            for i in self.graph[start]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        print()     


def main() -> None:
    g: Graph = Graph()
    n, m = [int(x) for x in input().split()]
    for _ in range(m):

        u, v = [int(x) for x in input().split()]
        g.add_edge(u, v)
    
    for edge in range(1, n+1):
        g.bfs(edge)
    
if __name__ == "__main__":
    main()