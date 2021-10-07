
def main():
    n, m = [int(x) for x in input().split()]
    graph = []

    for _ in range(m):
        sublist = int(input(2))
        graph.append(sublist)
    
    for i in range(m):
        print(f"vertex{i+1} connects with ", *graph[i])
    

if __name__ == "__main__":
    main()


