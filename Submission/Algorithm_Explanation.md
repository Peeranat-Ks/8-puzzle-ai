# Algorithm Explanations: 8-Puzzle Solver

This document explains the search algorithms and heuristics implemented in the 8-puzzle solver. The goal is to find a sequence of moves to transform an initial state into the goal state (1-8 ordered, with 0 as the empty tile).

## 1. Search Algorithms


The project uses a generic `tree_search` framework that utilizes a `Fringe` (Priority Queue) to manage the frontier of unexplored nodes. The difference between the algorithms lies in how they prioritize nodes in the fringe.

### 1.1 Greedy Best-First Search

**Concept:**
Greedy Best-First Search tries to expand the node that is closest to the goal, based solely on a heuristic evaluation function $h(n)$. It does not consider the cost of the path taken to reach the node.

*   **Evaluation Function:** $f(n) = h(n)$
    *   $h(n)$: Estimated cost from node $n$ to the goal.

**Implementation Details:**
*   **Fringe:** A priority queue where nodes are ordered by their heuristic value ($h$-value).
*   **Behavior:** It acts like "System 1" thinking (intuition). It makes locally optimal choices at each step.
*   **Properties:**
    *   **Complete:** No (can get stuck in loops, though our implementation uses a `visited` set to prevent this).
    *   **Optimal:** No. It may find a solution quickly, but it is not guaranteed to be the shortest path.
    *   **Efficiency:** generally faster than A* as it prunes the search space aggressively, but can go down wrong paths.

### 1.2 A* Search

**Concept:**
A* Search combines the cost to reach the node, $g(n)$, and the estimated cost to the goal, $h(n)$. It balances minimizing the total path cost.

*   **Evaluation Function:** $f(n) = g(n) + h(n)$
    *   $g(n)$: Actual cost from the start node to node $n$.
    *   $h(n)$: Estimated cost from node $n$ to the goal.

**Implementation Details:**
*   **Fringe:** A priority queue where nodes are ordered by their total estimated cost ($f$-value).
*   **Behavior:** It acts like "System 2" thinking (discernment). It systematically explores layers of the search space, ensuring it doesn't overlook a cheaper path.
*   **Properties:**
    *   **Complete:** Yes (unless there are infinitely many nodes with $f \le f(goal)$).
    *   **Optimal:** Yes, provided the heuristic $h(n)$ is *admissible* (never overestimates the true cost) and *consistent* (monotonic).
    *   **Efficiency:** Explores more nodes than Greedy BFS to guarantee optimality, making it slower and more memory-intensive for difficult puzzles.

---

## 2. Heuristics

The efficiency of both algorithms relies heavily on the quality of the heuristic function.

### 2.1 Heuristic 1: Misplaced Tiles ($h_1$)

**Definition:**
The number of tiles that are not in their goal position.

*   **Calculation:** Iterate through all 9 positions (0-8). If the tile at position $(r, c)$ is not the same as the tile in the goal state at $(r, c)$, increment the count. The blank tile (0) is typically excluded.
*   **Admissibility:** Yes. Every misplaced tile must move at least once to reach its correct position, so $h_1(n) \le C^*(n)$.
*   **Performance:** This is a weak heuristic. It doesn't capture *how far* the tiles are from their destinations.

### 2.2 Heuristic 2: Manhattan Distance ($h_2$)

**Definition:**
The sum of the horizontal and vertical distances of the tiles from their goal positions.

*   **Calculation:** For each tile from 1 to 8:
    $$ \text{distance} = |current\_row - goal\_row| + |current\_col - goal\_col| $$
    $$ h_2(n) = \sum \text{distance}_{\text{tile}} $$
*   **Admissibility:** Yes. A tile can only move one step closer to its goal (vertically or horizontally) in a single move. Thus, the total Manhattan distance is a lower bound on the number of moves required.
*   **Performance:** This is a stronger heuristic than $h_1$ because $h_2(n) \ge h_1(n)$ for all $n$. It guides the search more effectively, leading to fewer nodes expanded compared to Misplaced Tiles.

---

## 3. Data Structures

### Node Class
Represents a state in the search tree.
*   `state`: The 3x3 grid configuration.
*   `acc_cost` ($g$): The path cost from the start node.
*   `hval` ($h$ or $f$): The value used for sorting in the priority queue.
*   `parent`: Reference to the parent node (for path reconstruction).
*   `action`: The move (UP, DOWN, LEFT, RIGHT) that led to this state.

### Priority Queue (Fringe)
Standard Python `heapq` is used to implement the priority queue.
*   Stores tuples: `(priority, id(node), node)`
*   The `priority` is $h(n)$ for Greedy and $f(n)$ for A*.
*   The `id(node)` acts as a tie-breaker to ensure stability if two nodes have the same priority.

