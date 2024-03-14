from collections import deque

def is_valid(state):
    missionaries_left, cannibals_left, boat, missionaries_right, cannibals_right = state
    if missionaries_left < 0 or cannibals_left < 0 or missionaries_right < 0 or cannibals_right < 0:
        return False
    if missionaries_left > 0 and missionaries_left < cannibals_left:
        return False
    if missionaries_right > 0 and missionaries_right < cannibals_right:
        return False
    return True

def generate_next_states(state):
    missionaries_left, cannibals_left, boat, missionaries_right, cannibals_right = state
    next_states = []
    if boat == 'left':
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    next_state = (missionaries_left - m, cannibals_left - c, 'right', missionaries_right + m, cannibals_right + c)
                    if is_valid(next_state):
                        next_states.append(next_state)
    else:
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    next_state = (missionaries_left + m, cannibals_left + c, 'left', missionaries_right - m, cannibals_right - c)
                    if is_valid(next_state):
                        next_states.append(next_state)
    return next_states

def bfs():
    initial_state = (3, 3, 'left', 0, 0)
    if is_valid(initial_state):
        queue = deque([(initial_state, [])])
        while queue:
            state, path = queue.popleft()
            if state[0] == 0 and state[1] == 0 and state[2] == 'right':
                return path
            for next_state in generate_next_states(state):
                queue.append((next_state, path + [state]))
    return "No solution found."

def print_solution(path):
    for i, state in enumerate(path):
        missionaries_left, cannibals_left, boat, missionaries_right, cannibals_right = state
        print(f"Step {i+1}:")
        print(f"On the left side: {missionaries_left} missionaries, {cannibals_left} cannibals")
        print(f"On the right side: {missionaries_right} missionaries, {cannibals_right} cannibals")
        print(f"The boat is on the {boat} side.\n")

def main():
    solution_path = bfs()
    if solution_path:
        print("Solution found!")
        print_solution(solution_path)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
