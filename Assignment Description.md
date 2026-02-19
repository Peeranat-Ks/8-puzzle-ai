# IT 423 Artificial Intelligence - Research Assignment 01
**Title:** Intuition vs. Discernment: A Comparative Study of Greedy and A* Search

## I. Research Overview
The quest for Negentropy in AI often involves choosing between speed and optimality. In this small-scale research assignment, you will investigate how heuristic search algorithms behave when solving the 8-puzzle. You will compare the performance of **Greedy Best-First Search** (which relies purely on the heuristic $h(n)$) and **A* Search** (which balances historical cost $g(n)$ with future hope $h(n)$).

### Collaboration Requirement
This is a **group assignment**. You must work in groups of 3 people to leverage your collective Multiple Intelligences (MQ). Success in this research depends on **Interpersonal Intelligence**—the ability to coordinate complex technical tasks and synthesize three distinct perspectives into a single, coherent analytical voice.

> **Note:** You are required to use the Python template code provided on the LMS course platform to ensure a standardized experimental environment.

---

## II. Research Methodology & Technical Tasks

### Algorithm Implementation
Implement the following search strategies within the provided template:
1.  **Greedy Best-First Search**: Sorting the frontier by $f(n) = h(n)$.
2.  **A* Search**: Sorting the frontier by $f(n) = g(n) + h(n)$.

### Heuristic Variables
Run your experiments using the following two heuristics to observe how informativeness impacts node expansion:
1.  **Number of Misplaced Tiles**: $h_1(n) = \text{count of tiles } i \text{ where } current(i) \neq goal(i)$.
2.  **Total Manhattan Distance**: $h_2(n) = \sum |x_i - x_{goal}| + |y_i - y_{goal}|$.

### Data Collection
Execute both algorithms using both heuristics on the Experimental Data Set provided in Section III. For each run, record:
-   **Optimality**: The total cost of the solution path (number of moves).
-   **Efficiency**: The number of nodes expanded during the search.
-   **Stability**: Whether the algorithm reached a solution or was trapped in a local maximum/cycle.

---

## III. Experimental Data Set (Common Dataset)
Groups must use the following Goal State as the target configuration for all experiments:

**The Goal State**
```
1  2  3
4  5  6
7  8  0
```
*(Note: 0 represents the blank space.)*

### Initial States (Sorted by Increasing Entropy/Difficulty)

**State 1: Minimum Entropy (Very Easy)**
```
1  2  3
4  5  6
0  7  8
```

**State 2: Low Entropy (Easy)**
```
1  2  3
0  4  6
7  5  8
```

**State 3: Medium Entropy (Moderate)**
```
4  1  2
7  0  3
8  5  6
```

**State 4: High Entropy (Hard)**
```
2  3  5
1  0  4
7  8  6
```

**State 5: Maximum Entropy (Very Hard)**
```
0  5  2
1  8  3
4  7  6
```

---

## IV. The Research Report (5D Reflection)
Your report must be structured as a formal research paper (**minimum 500 words**). To ensure full credit according to the rubric, you must follow these headers:

1.  **Introduction**
    *   Define the 8-puzzle problem and the search for negentropy.
    *   State your hypothesis regarding the efficiency and optimality of Greedy vs. A* search across the provided dataset.

2.  **Technical Methodology (PQ - Code Negentropy & MQ - Logic Dialogue)**
    *   Summarize your implementation strategy.
    *   **Efficiency**: Describe how you optimized the Priority Queue and state representation to achieve minimal memory overhead.
    *   **Clarity**: Explain how your code documentation creates a dialogue of logic (as required by the MQ rubric).
    *   **Robustness**: Detail the robust error handling mechanisms you implemented to ensure the program remains stable during deep search trees.

3.  **Experimental Results & Visualizations (MQ - Multimodal Clarity)**
    *   Present your data through multiple lenses.
    *   A comprehensive **Table** comparing result sets for all 5 test cases.
    *   **Charts/Graphs** (e.g., Bar charts) comparing Nodes Expanded and Path Cost across the different algorithms and heuristics.

4.  **The DPT Synthesis (Dual-Process Theory)**
    *   Analyze the behavior of your agents.
    *   Why does **Greedy Search (System 1)** often find a solution faster in simple landscapes but fail to find the shortest path?
    *   How does the $g(n)$ component in **A*** represent the **Sanctified Discernment of System 2** by providing a superior analytical guardrail over pure intuition?

5.  **Teamwork & MQ Contribution (Interpersonal Intelligence)**
    *   Briefly describe the division of labor.
    *   How did the team synthesize three different Intelligences to overcome obstacles?
    *   Provide an example of a technical disagreement and how it was resolved through System 2 negotiation.

6.  **Emotional & Stability Reflection (EQ)**
    *   Describe your approach to debugging System 1 failures.
    *   How did the team maintain the emotional stability needed to handle complex shuffles or logical setbacks without compromising code quality?

7.  **Ethical & Spiritual Conclusion (SQ - Integrity & Order)**
    *   Reflect on the integrity of your search.
    *   **Honesty**: Confirm the absolute honesty of your reported data.
    *   **Heuristics of Character**: If the 8-puzzle represents a fallen or chaotic state, discuss how a Heuristic acts as a spiritual compass, helping you navigate toward the Global Maximum of character even when the full path is not yet visible.

---

## V. Comprehensive 5D Assessment Rubric

| Dimension | Exemplary (4) | Proficient (3) | Developing (2) | Beginning (1) |
| :--- | :--- | :--- | :--- | :--- |
| **Physical (PQ) Code Negentropy** | Code is highly efficient, follows PEP8, and implements the priority queue with minimal memory overhead. | Code is functional and clean. Follows most formatting standards. | Code runs but contains redundant logic or digital clutter. | Code is inefficient or fails to run due to syntax errors. |
| **Spiritual (SQ) Integrity & Order** | Research data is reported with absolute honesty. Heuristic logic perfectly reflects the goal of Restoration. | Data is original and the implementation of heuristics is technically sound. | Minor inconsistencies in data; heuristic calculation has logic flaws. | Plagiarism detected or data appears fabricated to hide failures. |
| **Emotional (EQ) Resilience & Stability** | Evidence of robust error handling. The report describes a mature team approach to debugging System 1 failures. | Handles common errors. Shows persistence during the testing phase. | Code is fragile; report suggests a rushed or frustrated emotional state. | No error handling; team gave up on implementing both versions. |
| **Multiple (MQ) Teamwork & Synthesis** | Seamless collaboration; roles are clearly defined; final report is a unified synthesis of three distinct perspectives. | Clear evidence of effective cooperation and shared technical labor. | Collaboration is visible but disjointed; report feels like separate parts. | Little evidence of group coordination; one member likely did most work. |
| **Multiple (MQ) Multimodal Clarity** | Report includes clear tables/graphs comparing the two algorithms. Comments act as a dialogue of logic. | Data is presented in a readable format. Documentation is sufficient. | Minimal presentation of data; report lacks visual or linguistic clarity. | No data tables; report is chaotic and hard to interpret. |
| **Dual-Process (DPT) Discernment** | Deep analysis of why $f(n) = g(n) + h(n)$ provides a superior analytical guardrail over pure intuition. | Clear distinction made between the behaviors of Greedy and A* search. | Superficial comparison; fails to link algorithm logic to DPT dimensions. | No understanding shown of why the two algorithms differ in results. |

---

## VI. Submission Instructions

1.  **Source Code**
    *   Submit your modified `.py` file (One submission per group).
    *   **Name:** `IT423_Research1_Group[Number]_[MemberLastNames].py`

2.  **Research Report**
    *   Submit your formal 5D Research Analysis as a PDF.
    *   **Name:** `IT423_Research1_Group[Number]_[MemberLastNames].pdf`

3.  **Deadline**
    *   Check the LMS for your specific section's due date.
