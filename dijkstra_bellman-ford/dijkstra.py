import math
from collections import defaultdict


class Vertex:
    

    def __init__(self, v: int, weigth: int = 0):
        self.v = v
        self.weight = weigth
        self.d = math.inf
        self.p = None


class Graph:
    
    
    def __init__(self, number_of_vertecies: int, number_of_edges: int):
        self.n = number_of_vertecies
        self.m = number_of_edges
        self.graph = defaultdict(list)
    

    def print_graph(self):

        for key, values in self.graph.items():
            for node in values:
                print(f"Edge {key} - {node.v}, w = {node.weight}")

        

        # for key in self.graph.keys():
        #     for lst in self.graph.values():
        #         for node in lst:
        #             print(f"Edge {key} - {node.v}, w = {node.weight}", end=" ")
        #         print()
        
    def add_edge(self, u: int, v: int, w: int):
        self.graph[u].append(Vertex(v, w))
        self.graph[v].append(Vertex(u, w))
    
    
    def dijkstra_shortes_path(self, s: Vertexto: int):
        pass

def main():

    n, m = [int(x) for x in input().split()]
    f, s = [int(x) for x in input().split()]

    g: Graph = Graph(n, m)

    for _ in range(m):
        u,v,w = [int(x) for x in input().split()]
        g.add_edge(u,v,w)
    
    g.print_graph()


if __name__ == "__main__":
    main()
    
        

