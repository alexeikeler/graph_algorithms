#Program to represent graph as an adjacency list

class Node:
	def __init__(self, key: int):
		self.vertex = key 
		self.next = None

class Graph:
	def __init__(self, vertices):
		self.V = vertices
		self.graph = [None] * self.V

	def insert(self, u: int, v: int) -> None:
		# Function to insert edge (u, v) into the graph
		# u - source node
		# v - destination node

		node = Node(u)
		node.next = self.graph[v]
		self.graph[v] = node

		node: Node = Node(v)
		node.next = self.graph[u]
		self.graph[u] = node

	def show_current(self, vertex: int):
		temp: Node = self.graph[vertex]
		#if temp is None:
		#	return
		while temp is not None:
			print(temp.vertex, end = " ")
			temp = temp.next
		print()

def main():
	vertex_count: int = int(input())
	operation_count: int = int(input())

	graph: Graph = Graph(vertex_count*2)

	for operation in range(operation_count):
		#operands = [int(x) for x in input().split()]
		operands: list = list(map(int, input().split()))
		if operands[0] == 1:
			graph.insert(operands[1], operands[2])
		elif operands[0] == 2:
			graph.show_current(operands[1])

if __name__ == "__main__":
	main()