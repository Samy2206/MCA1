# BFS Iterative
def bfs_iterative(graph, start):
    visited = []
    queue = [start]
    
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            for neighbor in graph[vertex]:  # Use a loop to add neighbors
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return visited

# DFS Iterative
def dfs_iterative(graph, start):
    visited = []
    stack = [start]
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            for neighbor in reversed(graph[vertex]):  # Add neighbors in reverse order to maintain order
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return visited

# BFS Recursive
def bfs_recursive(graph, queue, visited):
    if not queue:
        return visited
    
    vertex = queue.pop(0)
    if vertex not in visited:
        visited.append(vertex)
        for neighbor in graph[vertex]:  # Use a loop to add neighbors
            if neighbor not in visited:
                queue.append(neighbor)
    
    return bfs_recursive(graph, queue, visited)

# DFS Recursive
def dfs_recursive(graph, vertex, visited):
    if vertex not in visited:
        visited.append(vertex)
        for neighbor in graph[vertex]:  # Use a loop to recurse on neighbors
            dfs_recursive(graph, neighbor, visited)
    return visited



# Graph Representation using an Adjacency Dictionary
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Example Usage
print("BFS Iterative:", bfs_iterative(graph, 'A'))
print("DFS Iterative:", dfs_iterative(graph, 'A'))
print("BFS Recursive:", bfs_recursive(graph, ['A'], []))
print("DFS Recursive:", dfs_recursive(graph, 'A', []))
