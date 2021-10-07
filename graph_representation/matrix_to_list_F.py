def main():
	n: int = int(input())
	matrix: list = []
	for i in range(n):
		row = [int(x) for x in input().split()]
		matrix.append(row)
	
	adj_list: list = []
	for i in range(n):
		sublist = []
		adj_list.append(sublist)
		for j in range(n):
			if matrix[i][j] == 1:
				sublist.append(j+1)

	for lst in adj_list:
		print(len(lst), *lst)
	


if __name__ == "__main__":
	main()