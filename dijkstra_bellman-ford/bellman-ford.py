# Python3 program for Bellman-Ford's
# single source shortest path algorithm.
from sys import maxsize

def BellmanFord(graph, V, E, src):

    dis = [maxsize] * V

    dis[src] = 0

    for i in range(V - 1):
        for j in range(E):
            if dis[graph[j][0]] + \
            graph[j][2] < dis[graph[j][1]]:
                dis[graph[j][1]] = dis[graph[j][0]] + \
                                    graph[j][2]
    for i in range(E):
        x = graph[i][0]
        y = graph[i][1]
        weight = graph[i][2]
        if dis[x] != maxsize and dis[x] + \
                        weight < dis[y]:
            print("Graph contains negative weight cycle")
    
    for i in range(V):
        if dis[i] == maxsize: 
            dis[i] = 30000
    
    print(*dis)


def main():
    n,m = [int(x) for x in input().split()]
    
    if m == 0:
        print(30000)
        return
    
    graph = []
    
    for i in range(m):
        u,v,w = [int(x) for x in input().split()]
        graph.append([u-1, v-1, w])
    
    BellmanFord(graph, n,m,0)
if __name__ == "__main__":
    main()