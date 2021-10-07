def main():
    n: int = int(input())
    income: list = []
    outcome: list = []
    matrix: list = []
    temp: int = 0

    counter_income: int = 0
    counter_outcome: int = 0
    
    for i in range(n):
        row = [int(x) for x in input().split()]
        if sum(row) == 0:
            counter_income += 1
            income.append(i+1)
        matrix.append(row)

    for i in range(n):
        for j in range(n):
            temp += matrix[j][i]
        if temp == 0:
            counter_outcome += 1
            outcome.append(i + 1)
        temp = 0
    
    print(counter_outcome, *outcome)
    print(counter_income,*income)

if __name__ == "__main__":
    main()
