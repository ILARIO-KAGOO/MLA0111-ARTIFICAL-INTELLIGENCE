import random

# Define the objective function to be optimized
def objective_function(x):
    return -(x ** 2)  # Negate for maximizing instead of minimizing

# Hill climbing algorithm
def hill_climbing(max_iter=1000, step_size=0.1):
    # Initialize the current solution randomly
    current_solution = random.uniform(-10, 10)
    current_value = objective_function(current_solution)

    # Perform iterations
    for _ in range(max_iter):
        # Generate a new candidate solution by adding random noise
        candidate_solution = current_solution + random.uniform(-step_size, step_size)
        candidate_value = objective_function(candidate_solution)

        # Check if the candidate solution is better than the current solution
        if candidate_value > current_value:
            current_solution = candidate_solution
            current_value = candidate_value

    return current_solution, current_value

# Main function to run the hill climbing algorithm
def main():
    max_iter = 1000  # Maximum number of iterations
    step_size = 0.1  # Step size for generating neighboring solutions

    # Run the hill climbing algorithm
    solution, value = hill_climbing(max_iter, step_size)

    # Print the result
    print("Optimal Solution:", solution)
    print("Optimal Value:", value)

if __name__ == "__main__":
    main()
