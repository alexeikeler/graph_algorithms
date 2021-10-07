from collections import defaultdict
from typing import List, Union
import math


class Graph:
    
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.container = defaultdict(list)
    
    def add_edge(self, u: int, v: int) -> Union[List[int], List[bool]]:

        self.container[u].append(v)
        self.container[v].append(u)
    
    def bfs(self, start: int, end: int):
        
        q: List[int] = []
        dist: List[int] = [math.inf] * self.n
        parents: List[int] = [-1] * self.n
        

        q.insert(0, start)
        dist[start] = 0

        while len(q) > 0:
            current: int = q.pop()

            for next_node in self.container[current]:
    
                if dist[next_node] == math.inf:
                    dist[next_node] = dist[current] + 1
                    parents[next_node] = current
                    q.insert(0, next_node)
        
        #print("Dist array: ", dist)
        #print(f"dist to node {end + 1} from node {start + 1}: ", dist[end])

        return dist, parents

    def reconstruct_path(self, start: int, path_to: int, parents: List[int], d: List[int]) -> None:

        if d[path_to] == math.inf:
            print(-1)
            return

        path: List[int] = []
        v: int = path_to

        while v != start:
            path.append(v)
            v = parents[v]
        
        path.append(start)

        print(len(path)-1)
        print(*[x + 1 for x in path[::-1]])


def main():

    n, m = [int(x) for x in input().split()]
    s, e = [int(x) for x in input().split()]

    s -= 1
    e -= 1

    graph: Graph = Graph(n, m)

    for _ in range(m):

        u, v = [int(x) for x in input().split()]
        u -= 1
        v -= 1
        graph.add_edge(u, v)
    
    d, p = graph.bfs(s ,e)
    graph.reconstruct_path(s, e, p, d)
        
if __name__ == "__main__":
    main()

