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

Hypothesis: 
    1. Greedy Best-First Search (GBFS) is more efficient in comparison to A* but is not as optimal.
    2. A* Search is slower than GBFS but guarantees the most optimal solution. 

## 2. Technical Methodology (PQ - Code Negentropy & MQ - Logic Dialogue) - Morgan Phillip Matthew
*(Summarize your implementation strategy. Describe how you optimized the Priority Queue and state representation to achieve minimal memory overhead. Explain how your code documentation creates a dialogue of logic. Detail the robust error handling mechanisms implemented.)*


[Write your methodology here...]

## 3. Experimental Results & Visualizations (MQ - Multimodal Clarity) - Adelaide
*(Present your data through multiple lenses. Include a comprehensive table comparing result sets for all 5 test cases. Include charts/graphs comparing Nodes Expanded and Path Cost across the different algorithms and heuristics.)*

### Data Table

| Initial State | Greedy ($h_1$) Cost | Greedy ($h_1$) Nodes | Greedy ($h_1$) Time(us) | Greedy ($h_2$) Cost | Greedy ($h_2$) Nodes | Greedy ($h_2$) Time(us) | A* ($h_1$) Cost | A* ($h_1$) Nodes | A* ($h_1$) Time(us) | A* ($h_2$) Cost | A* ($h_2$) Nodes | A* ($h_2$) Time(us) | 
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | 
| State 1 (Very Easy) | 2 | 3 | 138 | 2 | 3 | 132 | 2 | 3 | 127 | 2 | 3 | 112 | 
| State 2 (Easy) | 3 | 4 | 181 | 3 | 4 | 176 | 3 | 4 | 134 | 3 | 4 | 207 |
| State 3 (Moderate) | 8 | 9 | 295 | 8 | 9 | 319 | 8 | 9 | 283 | 8 | 9 | 250 | 
| State 4 (Hard) | 8 | 579 | 4462 | 8 | 9 | 365 | 8 | 22 | 357 | 8 | 10 | 250 | 
| State 5 (Very Hard) | 8 | 9 | 261 | 8 | 9 | 283 | 8 | 9 | 256 | 8 | 9 | 326 |

### Analysis
[Write your analysis of the results here...]

## 4. The DPT Synthesis (Dual-Process Theory) - Morgan
*(Analyze the behavior of your agents. Why does Greedy Search (System 1) often find a solution faster in simple landscapes but fail to find the shortest path? How does the $g(n)$ component in A* represent the Sanctified Discernment of System 2?)*

[Write your DPT synthesis here...]

## 5. Teamwork & MQ Contribution (Interpersonal Intelligence) - Adelaide
*(Briefly describe the division of labor. How did the team synthesize three different Intelligences to overcome obstacles? Provide an example of a technical disagreement and how it was resolved through System 2 negotiation.)*

[Write your teamwork reflection here...]

## 6. Emotional & Stability Reflection (EQ) - Peeranat
*(Describe your approach to debugging System 1 failures. How did the team maintain the emotional stability needed to handle complex shuffles or logical setbacks without compromising code quality?)*

[Write your EQ reflection here...]

## 7. Ethical & Spiritual Conclusion (SQ - Integrity & Order) - Peeranat
*(Reflect on the integrity of your search. Confirm the absolute honesty of your reported data. Discuss how a Heuristic acts as a spiritual compass.)*

[Write your conclusion here...]

---
**Statement of Integrity:** We confirm that the data reported in this document is original and collected honestly from our own algorithm implementations.
