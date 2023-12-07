class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_list = [[] for _ in range(num_vertices)]
    
    def add_edge(self, source, destination, weight):
        self.adjacency_list[source].append((destination, weight))
        self.adjacency_list[destination].append((source, weight))  # For an undirected graph

def your_algorithm(graph):
    visited = [False] * graph.num_vertices
    total_weight = 0

    # Start from vertex 0
    visited[0] = True

    while False in visited:
        min_weight = float('inf')
        min_edge = None

        for source in range(graph.num_vertices):
            if visited[source]:
                for destination, weight in graph.adjacency_list[source]:
                    if not visited[destination] and weight < min_weight:
                        min_weight = weight
                        min_edge = (source, destination)

        if min_edge:
            source, destination = min_edge
            total_weight += min_weight
            visited[destination] = True
            print(f"Added edge: {source} - {destination} (Weight: {min_weight})")

    print(f"Total weight of MST: {total_weight}")

# Create the graph
graph = Graph(54)
graph.add_edge(0, 1, 46)
graph.add_edge(0, 6, 93)
graph.add_edge(1, 6, 17)
graph.add_edge(1, 7, 71)
graph.add_edge(1, 8, 34)
graph.add_edge(2, 3, 36)
graph.add_edge(2, 9, 86)
graph.add_edge(3, 9, 97)
graph.add_edge(4, 10, 76)
graph.add_edge(4, 11, 71)
graph.add_edge(4, 15, 10)
graph.add_edge(4, 21, 38)
graph.add_edge(5, 11, 18)
graph.add_edge(5, 16, 51)
graph.add_edge(6, 7, 95)
graph.add_edge(7, 8, 3)
graph.add_edge(7, 12, 19)
graph.add_edge(7, 17, 73)
graph.add_edge(8, 9, 61)
graph.add_edge(8, 12, 29)
graph.add_edge(8, 19, 36)
graph.add_edge(9, 13, 80)
graph.add_edge(9, 19, 93)
graph.add_edge(10, 13, 62)
graph.add_edge(10, 14, 55)
graph.add_edge(10, 20, 99)
graph.add_edge(11, 15, 55)
graph.add_edge(11, 16, 16)
graph.add_edge(12, 17, 30)
graph.add_edge(12, 18, 82)
graph.add_edge(12, 19, 93)
graph.add_edge(13, 19, 43)
graph.add_edge(13, 20, 8)
graph.add_edge(14, 20, 24)
graph.add_edge(14, 21, 70)
graph.add_edge(15, 16, 27)
graph.add_edge(15, 21, 54)
graph.add_edge(15, 24, 93)
graph.add_edge(15, 25, 38)
graph.add_edge(15, 26, 10)
graph.add_edge(16, 22, 6)
graph.add_edge(16, 24, 62)
graph.add_edge(18, 19, 42)
graph.add_edge(18, 28, 94)
graph.add_edge(18, 29, 80)
graph.add_edge(19, 20, 33)
graph.add_edge(19, 28, 20)
graph.add_edge(20, 21, 31)
graph.add_edge(20, 27, 40)
graph.add_edge(20, 28, 16)
graph.add_edge(21, 26, 59)
graph.add_edge(21, 27, 47)
graph.add_edge(22, 23, 33)
graph.add_edge(22, 24, 55)
graph.add_edge(23, 24, 80)
graph.add_edge(25, 26, 12)
graph.add_edge(25, 35, 98)
graph.add_edge(25, 36, 91)
graph.add_edge(26, 27, 97)
graph.add_edge(26, 35, 3)
graph.add_edge(27, 28, 26)
graph.add_edge(27, 34, 39)
graph.add_edge(27, 35, 88)
graph.add_edge(27, 43, 18)
graph.add_edge(28, 29, 35)
graph.add_edge(28, 33, 83)
graph.add_edge(28, 34, 36)
graph.add_edge(29, 30, 76)
graph.add_edge(29, 32, 72)
graph.add_edge(29, 46, 75)
graph.add_edge(30, 31, 22)
graph.add_edge(30, 32, 87)
graph.add_edge(30, 47, 62)
graph.add_edge(31, 47, 52)
graph.add_edge(32, 46, 1)
graph.add_edge(32, 47, 7)
graph.add_edge(32, 48, 75)
graph.add_edge(33, 34, 57)
graph.add_edge(33, 44, 82)
graph.add_edge(33, 45, 25)
graph.add_edge(33, 46, 13)
graph.add_edge(34, 43, 19)
graph.add_edge(34, 44, 78)
graph.add_edge(35, 36, 5)
graph.add_edge(35, 37, 33)
graph.add_edge(35, 43, 83)
graph.add_edge(36, 37, 59)
graph.add_edge(36, 39, 88)
graph.add_edge(37, 39, 39)
graph.add_edge(37, 40, 17)
graph.add_edge(37, 43, 39)
graph.add_edge(38, 39, 16)
graph.add_edge(38, 42, 91)
graph.add_edge(39, 40, 10)
graph.add_edge(39, 42, 23)
graph.add_edge(40, 41, 3)
graph.add_edge(40, 43, 76)
graph.add_edge(41, 43, 34)
graph.add_edge(41, 50, 47)
graph.add_edge(43, 44, 20)
graph.add_edge(43, 50, 64)
graph.add_edge(44, 45, 47)
graph.add_edge(44, 50, 26)
graph.add_edge(45, 46, 92)
graph.add_edge(45, 49, 82)
graph.add_edge(45, 50, 60)
graph.add_edge(45, 53, 9)
graph.add_edge(46, 48, 42)
graph.add_edge(46, 49, 23)
graph.add_edge(47, 48, 52)
graph.add_edge(48, 49, 17)
graph.add_edge(48, 51, 90)
graph.add_edge(48, 52, 33)
graph.add_edge(49, 52, 44)
graph.add_edge(49, 53, 55)
graph.add_edge(50, 53, 28)
graph.add_edge(51, 52, 52)


# Run your algorithm
your_algorithm(graph)
