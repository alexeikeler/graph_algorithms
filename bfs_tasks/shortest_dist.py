from typing import List
from collections import deque

def main():
    #n, start, end = [int(x) for x in input().split()]
    n, start = [int(x) for x in input().split()]
    start -= 1
    #end -= 1
    adj_matrix: List[List[int]] = []

    for _ in range(n):
        row = [int(x) for x in input().split()]
        adj_matrix.append(row)
    
    
    bfs(n, start, adj_matrix)

def bfs(n: int, start: int, adj_matrix: List[List[int]]):
    dist = [-1] * n
    #parent = [-1] * n

    q = []
    q.insert(0, start)
    dist[start] = 0
    
    while len(q) > 0:
        current = q.pop()
        for next in range(n):
            if (adj_matrix[current][next]) and (dist[next] == -1):
                dist[next] = dist[current] + 1
     #           parent[next] = current
                q.insert(0, next)
    
    #if dist[end] is not None:
    #    print(dist[end], end = " ")
    #
    #else:
    #    print(0, end = " ")
    
    print([x for x in dist])
    

if __name__ == "__main__":
    main()