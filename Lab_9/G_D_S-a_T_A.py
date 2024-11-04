from collections import deque

# Step 1: Implement the Graph Class
class Graph:
    def _init_(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)  # For undirected graph
    
    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {' '.join(map(str, self.graph[vertex]))}")

    # Step 2: Implement Depth-First Search (DFS)
    def dfs(self, start_vertex):
        visited = set()
        self._dfs_recursive(start_vertex, visited)
    
    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')
        
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

    # Step 3: Implement Breadth-First Search (BFS)
    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    # Step 4: Implement a Method to Find All Paths
    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in self.graph:
            return []
        paths = []
        for neighbor in self.graph[start_vertex]:
            if neighbor not in path:
                new_paths = self.find_all_paths(neighbor, end_vertex, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths

    # Step 5: Implement a Method to Check if the Graph is Connected
    def is_connected(self):
        if not self.graph:
            return True
        start_vertex = next(iter(self.graph))
        visited = set()
        self._dfs_recursive(start_vertex, visited)
        return len(visited) == len(self.graph)


    # Step 6: Implement a Method to Find the Shortest Path
    def find_shortest_path(self, start_vertex, end_vertex):
        if start_vertex not in self.graph or end_vertex not in self.graph:
            return None
        
        visited = set()
        queue = deque([(start_vertex, [start_vertex])])  # Store tuples of (vertex, path)

        while queue:
            vertex, path = queue.popleft()

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    if neighbor == end_vertex:
                        return path + [neighbor]  # Return the path to the end vertex
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return None  # No path found
    

    # Step 7: Implement a Method to Detect Cycles
    def has_cycle(self):
        visited = set()
        
        for vertex in self.graph:
            if vertex not in visited:
                if self._has_cycle_recursive(vertex, visited, -1):
                    return True
        return False

    def _has_cycle_recursive(self, vertex, visited, parent):
        visited.add(vertex)
        
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                if self._has_cycle_recursive(neighbor, visited, vertex):
                    return True
            elif neighbor != parent:  # A cycle is detected
                return True
        return False
    

    # Step 8: Implement a Method to Check if the Graph is Bipartite
    def is_bipartite(self):
        color = {}
        
        for vertex in self.graph:
            if vertex not in color:  # Not colored yet
                queue = deque([vertex])
                color[vertex] = 0  # Start coloring with color 0
                
                while queue:
                    current = queue.popleft()
                    
                    for neighbor in self.graph[current]:
                        if neighbor not in color:
                            # Assign alternate color to the neighbor
                            color[neighbor] = 1 - color[current]
                            queue.append(neighbor)
                        elif color[neighbor] == color[current]:
                            # If the neighbor has the same color, it's not bipartite
                            return False
        return True

    

# Test the Graph class
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

# Print the graph
print("Graph representation:")
g.print_graph()

# Test DFS
print("\nDFS starting from vertex 0:")
g.dfs(0)

# Test BFS
print("\nBFS starting from vertex 0:")
g.bfs(0)

# Test finding all paths
print("\nAll paths from vertex 0 to vertex 3:")
all_paths = g.find_all_paths(0, 3)
for path in all_paths:
    print(' -> '.join(map(str, path)))

# Test if the graph is connected
print("\nIs the graph connected?", g.is_connected())

# Add a disconnected vertex and test again
g.add_vertex(4)
print("After adding a disconnected vertex:")
print("Is the graph connected?", g.is_connected())


# Find and print the shortest path
shortest_path = g.find_shortest_path(0, 3)
print("\nShortest path from vertex 0 to vertex 3:", shortest_path)


# Check for cycles
print("\nDoes the graph contain a cycle?", g.has_cycle())


# Check if the graph is bipartite
print("\nIs the graph bipartite?", g.is_bipartite())