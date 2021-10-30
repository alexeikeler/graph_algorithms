from collections import defaultdict
from heapq import *

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen, mins = [(0,f,())], set(), {f: 0}
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return cost, path

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    print(-1)
    exit()

if __name__ == "__main__":
    n, m = [int(x) for x in input().split()]
    s, f = [int(x) for x in input().split()]
    
    edges = []

    for i in range(m):
        u,v,w = [int(x) for x in input().split()]
        edges.append((u,v,w))
        edges.append((v,u,w))
    
    print(*edges, sep = "\n")


    out = dijkstra(edges, s,f)
    print(out[0])
    aux=[]
    while len(out)>1:
        aux.append(out[0])
        out = out[1]
    aux.reverse()
    
    print(*[aux[i] for i in range(len(aux)-1)])