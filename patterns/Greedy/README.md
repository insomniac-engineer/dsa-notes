# Greedy Algorithms Types

![alt text](diagrams/greedy_classification.png)

## 1. Optimizing Greedy (Global Optimality)

* **Goal**: Find an an optimal/feasable choise under *global* constraint
* **Invariant**: The current state is the best possible prefix outcome.
* **Logic**: Every local step (iteration) preserves global invariant logic.
* **Examples**: Stocks, Gas Station, Jump Game.
* **Deep dive**:

  * [Optimizing Greedy Algorithm](optimizing_greedy_single_invariant.md)

## 2. Constructive Greedy (Parsing)

* **Goal**: Build a valid construction or translation.
* **Invariant**: The current prefix interpretation is logically sound and follows the rules (grammar).
 **Logic**: Every local step preserves global invariant logic.
* **Examples**: Roman to Integer, Integer to Roman.
* **Deep dive**: [Constructive Greedy Algorithm](constructive_greedy.md)

---

#### The "Look-Ahead" Rule (+1)

In many Greedy problems, the decision each iteration requires a peek at the next state to preserve the invariant:

* **Roman to Integer**: Peek `i + 1` to see if current is negative.
* **Gas Station**: We don't peek `i + 1` in the code, but the logic "forces" us to start fresh from `i + 1` if the invariant is violated.
