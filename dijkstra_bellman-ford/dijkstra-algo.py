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

    n, s, f = [int(x) for x in input().split()]

    s -= 1
    f -= 1

    graph = []

    for i in range(n):
        row = [int(x) for x in input().split()]
        for j in range(n):
            if row[j] != -1:
                graph.append((i, j, row[j]))

    show(graph, n)

    out = dijkstra(graph, s, f)
    print(out[0])


def show(graph, n):
    for i in range(len(graph)):
        print(*graph[i])


if __name__ == "__main__":
    main()
