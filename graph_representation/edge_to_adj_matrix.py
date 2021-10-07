def main():
    n,m = [int(number) for number in input().split()]
    matrix: list = [[0 for x in range(n)] for y in range(n)]
    
    for _ in range(m, 0, -1):
        u, v = [int(x) for x in input().split()]
        matrix[u-1][v-1] = 1
        matrix[v-1][u-1] = 1
        

    for row in matrix:
        print(*row)


if __name__ == "__main__":
    main()