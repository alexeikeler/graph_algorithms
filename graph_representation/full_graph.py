def main():
    vertex_count, edge_count = [int(x) for x in input().split()]
    vertecies = set()

    for _ in range(edge_count):
        vertecies.add(input())
    #print(len(vertecies))
    if ((vertex_count ** 2 - vertex_count)  // 2) == len(vertecies):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()