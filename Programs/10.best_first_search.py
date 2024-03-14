from queue import PriorityQueue

# Define a graph as an adjacency list
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'D': 5, 'E': 2},
    'C': {'F': 4},
    'D': {'G': 6},
    'E': {'H': 1},
    'F': {},
    'G': {},
    'H': {}
}

# Function to perform Best-First Search
def best_first_search(graph, start, goal):
    explored = set()  # Set to keep track of explored nodes
    frontier = PriorityQueue()  # Priority queue to store frontier nodes
    frontier.put((0, start))  # Initialize the frontier with the start node
    
    while not frontier.empty():
        cost, current_node = frontier.get()  # Get the node with the lowest cost from the frontier
        explored.add(current_node)  # Mark the current node as explored
        
        if current_node == goal:
            print("Goal reached:", current_node)
            return True
        
        for neighbor, neighbor_cost in graph[current_node].items():
            if neighbor not in explored:
                frontier.put((neighbor_cost, neighbor))  # Add neighbor to the frontier with its cost
    
    print("Goal not found")
    return False

# Example usage
start_node = 'A'
goal_node = 'H'
print("Starting Best-First Search from node", start_node, "to node", goal_node)
best_first_search(graph, start_node, goal_node)
