## Deep Classification of Greedy

Based on the nature of the "Correctness" invariant:

### 1. Optimizing Greedy (Global Optimality)
* **Goal**: Find the absolute maximum or minimum.
* **Invariant**: The current state is the best possible prefix outcome.
* **Logic**: Every local step contributes to the global peak.
* **Examples**: Stocks, Gas Station, Jump Game.

### 2. Constructive / Parsing Greedy (Validity)
* **Goal**: Build a valid construction or translation.
* **Invariant**: The current prefix interpretation is logically sound and follows the rules (grammar).
* **Logic**: Use "look-ahead" (e.g., `i + 1`) to decide the current symbol's role immediately.
* **Examples**: Roman to Integer, Integer to Roman.

---

## The "Look-Ahead" Rule (+1)

In many Greedy problems, the **Local Decision** requires a peek at the next state to preserve the invariant:
- **Roman to Integer**: Peek `i + 1` to see if current is negative.
- **Gas Station**: We don't peek `i + 1` in the code, but the logic "forces" us to start fresh from `i + 1` if the invariant is violated.