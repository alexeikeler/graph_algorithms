def main():
    n: int = int(input())
    matrix: list = []
    for i in range(n):
        row: list = [int(x) for x in input().split()]
        matrix.append(row)
        if matrix[i][i] == 1:
            print("YES")
            return
    print("NO")

if __name__ == "__main__":
    main()