def main():
    n: int = int(input())
    matrix: list = []
    income: list = []
    outcome: list = []
    temp: int = 0

    for i in range(n):
        
        row: list = [int(x) for x in input().split()]
        matrix.append(row)
        income.append(sum(row))
    
    for i in range(n):
        for j in range(n):
            temp += matrix[j][i]
        outcome.append(temp)
        temp = 0

    for i in range(n):
        print(outcome[i], income[i])
    
if __name__ == "__main__":
    main()