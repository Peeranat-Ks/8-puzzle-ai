# Research Report: Intuition vs. Discernment
**A Comparative Study of Greedy and A* Search**

*   **Course:** IT 423 Artificial Intelligence
*   **Group Number:**
*   **Team Members:**
    1.  202200272 | Peeranat Kongsang
    2.  202300155 | Adelaide Silverline Francis
    3.  202200154 | Matthew Philip Morgan
*   **Date: 23 February 2026**

## 1. Introduction
The 8-puzzle problem consists of a 3x3 board containing numbered tiles from 1 to 8. The remaining tile is left empty thus allowing for adjacent movements (left, right, up, and down) to be made. Negentropy is established when the configured goal state has been achived, which is usually a sequential order of the tiles.  

* **Hypothesis:** 
    1.  Greedy Best-First Search (GBFS) is more efficient in comparison to A* but is not as optimal.
    2.  A* Search is slower than GBFS but guarantees the most optimal solution. 

## 2. Technical Methodology (PQ - Code Negentropy & MQ - Logic Dialogue) - Morgan Phillip Matthew
**Implementation Strategy & Efficiency (PQ Optimization)**

Our implementation strategy centers on an object-oriented design using a generic tree_search framework that dynamically accepts different Fringe instances to seamlessly switch between Greedy and A* behaviors. To achieve code negentropy and minimal memory overhead, we optimized our Priority Queue by utilizing Python's built-in heapq module. Rather than pushing heavy, complex objects to the queue, the queue evaluates lightweight tuples formatted as (priority, id(node), node). The deliberate use of id(node) acts as an ultra-efficient tie-breaker; if two nodes share the same heuristic value, the queue relies on their unique memory addresses rather than expending computational overhead trying to compare the Node objects directly.

Furthermore, we optimized our state representation by defining the 3x3 puzzle grid as a nested tuple of tuples (e.g., ((1, 2, 3), (4, 5, 6), (7, 8, 0))). Because tuples are immutable, they are inherently hashable, which allowed us to store previously visited states in an explored set. This approach minimizes memory consumption and enables $O(1)$ constant-time lookups during graph search validation.

**Clarity (Logic Dialogue)**
To ensure our codebase acts as a clear dialogue of logic, we integrated comprehensive docstrings and inline comments that articulate the reasoning behind our technical decisions. Rather than simply dictating what the code does, the documentation explains the why. For instance, inline comments explicitly map the theoretical Dual-Process concepts to the codebase, such as labeling the A* calculation with # A*: f(n) = g(n) + h(n) and highlighting our graph search filter with # Optimization: Graph search check. This transparent, readable narrative guides the reviewer effortlessly through the team's problem-solving process.

**Robustness & Error Handling**
To guarantee programmatic stability when navigating deep search trees and high-entropy initial states, we implemented robust structural protections. The primary mechanism is our graph search architecture; by checking the hashable state against the explored set before expanding a node, we strictly prevent the search agents from getting trapped in infinite loops or cyclical paths. Additionally, the main execution environment includes structural input validation. If a user provides an invalid selection for the initial state or algorithm choice, the system catches the error, prevents a fatal crash, and safely prompts the user to try again or falls back to a default execution state.

## 3. Experimental Results & Visualizations (MQ - Multimodal Clarity) - Adelaide
### Data Table

The data table presents a comparison of GBFS and A\* Search combined with the different heuristics -- $h_1$ (Misplaced Tiles) and $h_2$ (Manhanttan Distances) -- applied to five different initial states. The performance metrics evaluated are the Path Cost (optimality), Nodes Expanded (efficiency), and Time (computational speed).


| Initial State | Greedy ($h_1$) Cost | Greedy ($h_1$) Nodes | Greedy ($h_1$) Time(us) | Greedy ($h_2$) Cost | Greedy ($h_2$) Nodes | Greedy ($h_2$) Time(us) | A* ($h_1$) Cost | A* ($h_1$) Nodes | A* ($h_1$) Time(us) | A* ($h_2$) Cost | A* ($h_2$) Nodes | A* ($h_2$) Time(us) | 
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | 
| State 1 (Very Easy) | 2 | 3 | 138 | 2 | 3 | 132 | 2 | 3 | 127 | 2 | 3 | 112 | 
| State 2 (Easy) | 3 | 4 | 181 | 3 | 4 | 176 | 3 | 4 | 134 | 3 | 4 | 207 |
| State 3 (Moderate) | 8 | 9 | 295 | 8 | 9 | 319 | 8 | 9 | 283 | 8 | 9 | 250 | 
| State 4 (Hard) | 8 | 579 | 4462 | 8 | 9 | 365 | 8 | 22 | 357 | 8 | 10 | 250 | 
| State 5 (Very Hard) | 8 | 9 | 261 | 8 | 9 | 283 | 8 | 9 | 256 | 8 | 9 | 326 |

### Analysis
##### A. Optimality:
All four algorithm-heuristic combinations return solutions with the same path cost for each individual state. This indicates that all methods successfully found optimal solutions for these particular instances. However, it is noteworthy to mention that GBFS does not inherently guaranteed to find the shortest path, but in these specific cases, the hueristics guided GBFS towards the most optimal path. 
##### B. Efficiency:
At Stage 4 (Hard), a massive spike anomaly occured as GBFS ($h_1$) expanded 579 nodes. This behaviour illustrates the "greedy" trap where $h_1$ blindly leads the search down a promising-looking but ultimately long path before finding the goal state, forcing it to explore a vast number of nodes. 

GBFS ($h_2$) outperforms $h_1$ by a huge margin. This implies that $h_2$ is a much more informative heuristic for this specific problem as it provide better guidance that prevents the search from going astray. For A\*, $h_2$ also shows better efficiency (10 nodes vs 22 nodes in State 4). 

Finally, when comparing GBFS and A\*, with $h_1$ A\* (22 nodes) is significantly more efficient than GBFS (579 nodes) in State 4. With $h_2$, the performance of GBFS (9 nodes) and A\* (10 nodes) is nearly identical. For the other states (1, 2, 3, 5), all algorithms expanded a nearly identical and very small number of nodes. This general trend reveals that the solution paths may have minimal branching or that the heuristic guidance is unambiguous enough. 
##### C. Computational Speed:
Executime time for each algorithms generally correlates with the number of nodes expanded. The most significant outlier is GBFS ($h_1$) in State 4, which took 4492 $\mu s$. Interestingly, A\* is not consistently slower. In State 2, A\* ($h_1$) is faster than GBFS ($h_1$) despite processing the same number of nodes (4). On the other hand, In State 5, A\* ($h_2$) is the slowest (326 $\mu s$) even though all four algorithms expanded donly 9 nodes.


## 4. The DPT Synthesis (Dual-Process Theory) - Morgan
In Dual-Process Theory, Greedy Best-First Search acts as System 1, relying entirely on intuition via the heuristic evaluation function $f(n) = h(n)$. In simple landscapes, this intuitive approach allows Greedy Search to rapidly find a solution because it makes locally optimal choices at each step to minimize the estimated distance to the goal. However, System 1 often fails to find the shortest path because it does not consider the cost of the path taken to reach the node. This lack of historical context makes it susceptible to "greedy traps," where it blindly follows a locally promising path that ultimately becomes a long, inefficient detour.

Conversely, A* Search embodies System 2 thinking, representing deliberative discernment. The inclusion of the $g(n)$ component introduces the actual historical cost from the start node into the evaluation function $f(n) = g(n) + h(n)$. This $g(n)$ component acts as the "Sanctified Discernment" of System 2, providing a superior analytical guardrail over pure intuition. By balancing the historical cost to reach the node with the estimated future cost to the goal, A* systematically explores layers of the search space, ensuring it does not overlook a cheaper path and guaranteeing optimality.



## 5. Teamwork & MQ Contribution (Interpersonal Intelligence) - Adelaide
*(Briefly describe the division of labor. How did the team synthesize three different Intelligences to overcome obstacles? Provide an example of a technical disagreement and how it was resolved through System 2 negotiation.)*

[Write your teamwork reflection here...]

## 6. Emotional & Stability Reflection (EQ) - Peeranat
### Reflection on Project Challenges
This project taught us the importance of staying calm under pressure. When we saw that GBFS expanded 579 nodes in State 4, we were surprised and frustrated. However, instead of giving up, we took time to carefully examine what happened. By staying patient and analyzing the results step by step, we turned confusion into understanding. This experience shows that solving algorithm problems requires both strong technical skills and the ability to handle emotions well—accepting when things don't go as planned, staying curious about unexpected outcomes, and treating mistakes as chances to learn rather than signs of failure.


## 7. Ethical & Spiritual Conclusion (SQ - Integrity & Order) - Peeranat
Working on this project taught us a big lesson in humility. We learned that we cannot just trust what we think we know; we have to look for the truth in the results. For example, when our code ran much slower than expected (expanding 579 nodes), it was a moment to practice patience instead of frustration. This taught us to let go of our pride and our initial guesses. By waiting to see the full picture before judging, we practiced true discernment—seeing things as they really are, not just how we want them to be. This habit helps us grow not just as programmers, but as people who value truth over our own opinions.

**Statement of Integrity:** We confirm that the data reported in this document is original and collected honestly from our own algorithm implementations.
