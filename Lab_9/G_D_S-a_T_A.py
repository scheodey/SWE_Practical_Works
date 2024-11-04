from collections import deque

class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = set()
    
    def add_edge(self, vertex1, vertex2):
        """Add an undirected edge between two vertices."""
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.adjacency_list[vertex1].add(vertex2)
        self.adjacency_list[vertex2].add(vertex1)

    def display(self):
        """Display the graph as an adjacency list."""
        for vertex, neighbors in self.adjacency_list.items():
            print(f"{vertex}: {' '.join(map(str, neighbors))}")

    def dfs(self, start_vertex):
        """Perform Depth-First Search (DFS)."""
        visited = set()
        self._dfs_helper(start_vertex, visited)
    
    def _dfs_helper(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')
        
        for neighbor in self.adjacency_list[vertex]:
            if neighbor not in visited:
                self._dfs_helper(neighbor, visited)

    def bfs(self, start_vertex):
        """Perform Breadth-First Search (BFS)."""
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')

            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def find_all_paths(self, start_vertex, end_vertex):
        """Find all paths between two vertices."""
        paths = []
        self._find_paths_helper(start_vertex, end_vertex, [], paths)
        return paths

    def _find_paths_helper(self, current, end, path, paths):
        path.append(current)
        
        if current == end:
            paths.append(list(path))
        else:
            for neighbor in self.adjacency_list.get(current, []):
                if neighbor not in path:
                    self._find_paths_helper(neighbor, end, path, paths)
        
        path.pop()

    def is_connected(self):
        """Check if the graph is connected."""
        if not self.adjacency_list:
            return True
        start_vertex = next(iter(self.adjacency_list))
        visited = set()
        self._dfs_helper(start_vertex, visited)
        return len(visited) == len(self.adjacency_list)

    def find_shortest_path(self, start_vertex, end_vertex):
        """Find the shortest path using BFS."""
        if start_vertex not in self.adjacency_list or end_vertex not in self.adjacency_list:
            return None
        
        queue = deque([(start_vertex, [start_vertex])])
        visited = set()

        while queue:
            vertex, path = queue.popleft()
            if vertex == end_vertex:
                return path

            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return None

    def has_cycle(self):
        """Detect cycles in the graph."""
        visited = set()
        
        for vertex in self.adjacency_list:
            if vertex not in visited:
                if self._cycle_helper(vertex, visited, None):
                    return True
        return False

    def _cycle_helper(self, vertex, visited, parent):
        visited.add(vertex)
        
        for neighbor in self.adjacency_list[vertex]:
            if neighbor not in visited:
                if self._cycle_helper(neighbor, visited, vertex):
                    return True
            elif neighbor != parent:
                return True
        return False

    def is_bipartite(self):
        """Check if the graph is bipartite."""
        color = {}
        
        for vertex in self.adjacency_list:
            if vertex not in color:
                queue = deque([vertex])
                color[vertex] = 0
                
                while queue:
                    current = queue.popleft()
                    for neighbor in self.adjacency_list[current]:
                        if neighbor not in color:
                            color[neighbor] = 1 - color[current]
                            queue.append(neighbor)
                        elif color[neighbor] == color[current]:
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
g.display()

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
