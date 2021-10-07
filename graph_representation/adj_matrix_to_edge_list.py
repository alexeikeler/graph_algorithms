def main():
    n: int = int(input())
    matrix: list = [[int(row) for row in input().split()] for _ in range(n)]

    for i in range(n):
        for j in range(i, n):
            if matrix[i][j] & matrix[j][i]:
                print(i+1, j+1)

if __name__ == "__main__":
    main()