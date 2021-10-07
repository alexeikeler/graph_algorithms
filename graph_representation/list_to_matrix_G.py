def main():
	n: int = int(input())
	adj_list = []
	matrix = [[0 for x in range(n)] for y in range(n)]
	for i in range(n):
		sublist = [int(x) for x in input().split()]
		adj_list.append(sublist)

	for i in range(n):
		temp = adj_list[i]
		for j in range(len(temp)-1):
			#print("temp j = ", temp[j])
			matrix[i][temp[j+1] - 1] = 1

	for row in matrix:
		print(*row)


if __name__ == '__main__':
	main()

