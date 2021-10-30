from collections import defaultdict
from heapq import *


def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))

    q, seen, mins = [(0, f, ())], set(), {f: 0}
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t:
                return cost, path

            for c, v2 in g.get(v1, ()):
                if v2 in seen:
                    continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    print(-1)
    exit()


def main():

    n = int(input())
    weights = [int(x) for x in input().split()]
    m = int(input())

    if m == 0 or n == 1:
        print(-1)
        return
        
    s = 0
    f = n - 1

    edges = [int(x) for x in input().split()]

    graph = [[] for i in range(n)]

    for i in range(m+1):
        u, v = [int(x) for x in input().split()]
        graph[u][v] = weights[u]
        graph[v][u] = weights[v]
    

    # print(*graph, sep ="\n")

    out = dijkstra(graph, s, f)
    print(out[0])


if __name__ == "__main__":
    main()