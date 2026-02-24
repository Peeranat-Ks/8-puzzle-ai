import copy 
import abc
import time
import heapq
import math

# ==========================================
# Global Parameters & Constants
# ==========================================

# The Goal State configuration
GOAL_STATE = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

# Initial States (from Assignment Description)
INITIAL_STATES = {
    "State 1 (Very Easy)": (
        (1, 2, 3),
        (4, 5, 6),
        (0, 7, 8)
    ),
    "State 2 (Easy)": (
        (1, 2, 3),
        (0, 4, 6),
        (7, 5, 8)
    ),
    "State 3 (Moderate)": (
        (4, 1, 2),
        (7, 0, 3),
        (8, 5, 6)
    ),
    "State 4 (Hard)": (
        (2, 3, 5),
        (1, 0, 4),
        (7, 8, 6)
    ),
    "State 5 (Very Hard)": (
        (0, 5, 2),
        (1, 8, 3),
        (4, 7, 6)
    )
}

# ==========================================
# Data Structures
# ==========================================

class Node:
    def __init__(self, state, acc_cost, depth, action, predecessor, hval = math.inf):
        self.__state = state
        self.__acc_cost = acc_cost
        self.__depth = depth
        self.__action = action
        self.__predecessor = predecessor
        self.__hval = hval

    def get_state(self):
        return self.__state
    
    def get_acc_cost(self):
        return self.__acc_cost
    
    def get_depth(self):
        return self.__depth
    
    def get_action(self):
        return self.__action

    def get_predecessor(self):
        return self.__predecessor
    
    def get_hval(self):
        return self.__hval
    
    def set_hval(self, hval):
        self.__hval = hval
    
    # Enables comparison of nodes for the Priority Queue
    def __lt__(self, other):
        # Tie-breaking for stability: If h-vals are equal, prefer lower depth or just stability
        return self.__hval < other.__hval

    def __repr__(self):
        return f"Node(h={self.__hval}, g={self.__acc_cost}, state={self.__state})"


class Problem:
    def __init__(self, initial_state, goal_state=GOAL_STATE):
        self.__initial_state = initial_state
        self.__goal_state = goal_state

    def get_initial_state(self):
        return self.__initial_state
    
    def test_goal(self, state):
        return state == self.__goal_state

    def step_cost(self, node, next_state):
        return 1

    def get_successor(self, state):
        """
        Generates valid successor states by sliding the blank tile (0).
        Returns a list of (action, new_state) tuples.
        """
        successors = []
        
        # Find 0
        blank_r, blank_c = None, None
        for r in range(3):
            for c in range(3):
                if state[r][c] == 0:
                    blank_r, blank_c = r, c
                    break
        
        # Moves: Up, Down, Left, Right
        moves = [
            (-1, 0, "UP"),
            (1, 0, "DOWN"),
            (0, -1, "LEFT"),
            (0, 1, "RIGHT")
        ]
        
        for dr, dc, action in moves:
            new_r, new_c = blank_r + dr, blank_c + dc
            
            # Check bounds
            if 0 <= new_r < 3 and 0 <= new_c < 3:
                # Convert tuple to list to swap
                new_state_list = [list(row) for row in state]
                new_state_list[blank_r][blank_c], new_state_list[new_r][new_c] = \
                    new_state_list[new_r][new_c], new_state_list[blank_r][blank_c]
                
                # Convert back to tuple
                new_state_tuple = tuple(tuple(row) for row in new_state_list)
                successors.append((action, new_state_tuple))
                
        return successors

    def expand(self, node):
        successors = []
        for (action, result) in self.get_successor(node.get_state()):
            s = Node(
                result, 
                node.get_acc_cost() + self.step_cost(node, result),
                node.get_depth() + 1,
                action,
                node
            )
            successors.append(s)
        return successors
    
    def solution(self, node):
        sol = []
        # Calculate final cost from the goal node
        cost = node.get_acc_cost() 
        while node is not None:
             # Skip root node's None action
            if node.get_action():
                sol.append(node.get_action())
            node = node.get_predecessor()
        sol.reverse()
        return sol, cost

# ==========================================
# Fringe Classes
# ==========================================

class Fringe(abc.ABC): 
    def add(self, node):
        pass
    def insert_all(self, list_of_nodes):
        pass
    def pop(self):
        pass
    def empty(self):
        pass
    def __len__(self):
        pass

class GreedyFringe(Fringe):
    def __init__(self, heuristic_func):
        super().__init__()
        self.__queue = []
        self.heuristic_func = heuristic_func
        self.nodes_expanded = 0 # Track efficiency

    def add(self, node):
        # Greedy: f(n) = h(n)
        h = self.heuristic_func(node.get_state())
        node.set_hval(h)
        # Using id(node) as tie-breaker to avoid comparing nodes directly if hvals are equal
        heapq.heappush(self.__queue, (node.get_hval(), id(node), node))

    def insert_all(self, list_of_nodes):
        for n in list_of_nodes:
            self.add(n)

    def pop(self):
        self.nodes_expanded += 1
        return heapq.heappop(self.__queue)[2]
    
    def empty(self):
        return len(self.__queue) == 0
    
    def __len__(self):
        return len(self.__queue)

class AStarFringe(Fringe):
    def __init__(self, heuristic_func):
        super().__init__()
        self.__queue = []
        self.heuristic_func = heuristic_func
        self.nodes_expanded = 0 # Track efficiency

    def add(self, node):
        # A*: f(n) = g(n) + h(n)
        h = self.heuristic_func(node.get_state())
        g = node.get_acc_cost()
        node.set_hval(g + h) # We store f(n) in the hval attribute for the PQ
        heapq.heappush(self.__queue, (node.get_hval(), id(node), node))

    def insert_all(self, list_of_nodes):
        for n in list_of_nodes:
            self.add(n)

    def pop(self):
        self.nodes_expanded += 1
        return heapq.heappop(self.__queue)[2]
    
    def empty(self):
        return len(self.__queue) == 0
    
    def __len__(self):
        return len(self.__queue)

# ==========================================
# Heuristic Functions
# ==========================================

def h1_misplaced_tiles(state):
    """
    Heuristic 1: Count of tiles i where current(i) != goal(i).
    """
    count = 0
    # Loop through grid
    for r in range(3):
        for c in range(3):
            val = state[r][c]
            # Ignore blank space (0)
            if val != 0:
                if val != GOAL_STATE[r][c]:
                    count += 1
    return count

def h2_manhattan_distance(state):
    """
    Heuristic 2: Sum of Manhattan distances.
    """
    distance = 0
    # Target positions cache for 1-8
    # 1:(0,0), 2:(0,1), 3:(0,2)
    # 4:(1,0), 5:(1,1), 6:(1,2)
    # 7:(2,0), 8:(2,1)
    # This matches the GOAL_STATE
    goal_positions = {
        1: (0,0), 2: (0,1), 3: (0,2),
        4: (1,0), 5: (1,1), 6: (1,2),
        7: (2,0), 8: (2,1)
    }
    
    for r in range(3):
        for c in range(3):
            val = state[r][c]
            if val != 0:
                if val in goal_positions:
                    target_r, target_c = goal_positions[val]
                    distance += abs(r - target_r) + abs(c - target_c)
    return distance

# ==========================================
# Tree Search Engine
# ==========================================

def tree_search(problem, fringe):
    """
    Returns (solution_path, cost, nodes_expanded, stability)
    """
    # Create initial node
    initial_node = Node(problem.get_initial_state(), 0, 0, None, None)
    fringe.add(initial_node)
    
    # Graph Search: Keep track of explored states to prevent cycles
    explored = set()
    
    while not fringe.empty():
        node = fringe.pop() # Remove from the front of the list.
        
        # Optimization: Graph search check
        if node.get_state() in explored:
            continue
        explored.add(node.get_state())
        
        # Goal check
        if problem.test_goal(node.get_state()):
            path, cost = problem.solution(node)
            return path, cost, fringe.nodes_expanded, "Solved"
        
        # Expansion
        successors = problem.expand(node)
        fringe.insert_all(successors)
        
    return None, 0, fringe.nodes_expanded, "Failed"

# ==========================================
# Main Execution
# ==========================================

if __name__ == "__main__":
    
    configurations = [
        ("State 1 (Very Easy)", INITIAL_STATES["State 1 (Very Easy)"]),
        ("State 2 (Easy)", INITIAL_STATES["State 2 (Easy)"]),
        ("State 3 (Moderate)", INITIAL_STATES["State 3 (Moderate)"]),
        ("State 4 (Hard)", INITIAL_STATES["State 4 (Hard)"]),
        ("State 5 (Very Hard)", INITIAL_STATES["State 5 (Very Hard)"])
    ]
    
    # List of algorithms to run: (Name, FringeClass, HeuristicFunc)
    algorithms = [
        ("Greedy BFS", GreedyFringe, h1_misplaced_tiles),
        ("Greedy BFS", GreedyFringe, h2_manhattan_distance),
        ("A* Search", AStarFringe, h1_misplaced_tiles),
        ("A* Search", AStarFringe, h2_manhattan_distance)
    ]

    while True:
        print("\n--- 8-Puzzle Solver Menu ---")
        print("Select Initial State:")
        for i, (name, _) in enumerate(configurations):
            print(f"{i + 1}. {name}")
        print("A. Run All")
        print("Q. Quit")
        
        choice_state = input("Enter choice (1-5, A, Q): ").strip().upper()
        
        if choice_state == 'Q':
            break
        
        selected_states = []
        if choice_state == 'A':
            selected_states = configurations
        elif choice_state.isdigit() and 1 <= int(choice_state) <= len(configurations):
            selected_states = [configurations[int(choice_state) - 1]]
        else:
            print("Invalid selection. Please try again.")
            continue

        selected_algorithms = []
        
        print("\nSelect Algorithm:")
        for i, (name, _, heuristic) in enumerate(algorithms):
            print(f"{i + 1}. {name} with {heuristic.__name__}")
        print("A. Run All Algorithms")
        
        choice_alg = input("Enter choice (1-4, A): ").strip().upper()
        
        if choice_alg == 'A':
            selected_algorithms = algorithms
        elif choice_alg.isdigit() and 1 <= int(choice_alg) <= len(algorithms):
            selected_algorithms = [algorithms[int(choice_alg) - 1]]
        else:
            print("Invalid selection. Defaulting to All Algorithms.")
            selected_algorithms = algorithms

        print(f"\n{'State':<20} | {'Algorithm':<15} | {'Heuristic':<20} | {'Status':<8} | {'Cost':<5} | {'Expanded':<10} | {'Time (s)':<10}")
        print("-" * 110)

        for state_name, initial_state in selected_states:
            for alg_name, fringe_class, heuristic in selected_algorithms:
                # Setup Problem
                problem = Problem(initial_state)
                fringe = fringe_class(heuristic)
                
                start_time = time.time()
                path, cost, expanded, status = tree_search(problem, fringe)
                end_time = time.time()
                
                heuristic_name = heuristic.__name__
                elapsed_time = end_time - start_time
                
                print(f"{state_name:<20} | {alg_name:<15} | {heuristic_name:<20} | {status:<8} | {cost:<5} | {expanded:<10} | {elapsed_time:.6f}")
                
                # Print Solution Path if user wants to observe
                if path and len(path) > 0:
                    print(f"Solution Path ({len(path)} steps): {path}")
                else:
                    print("No solution path found or empty.")

                input("\nPress Enter to continue to next run...")

