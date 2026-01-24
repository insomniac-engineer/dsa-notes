# Deep Classification of Greedy

![alt text](image.png)

## 1. Optimizing Greedy (Global Optimality)

* **Goal**: Find an an optimal/feasable choise under global constraint
* **Invariant**: The current state is the best possible prefix outcome.
* **Logic**: Every local step preserves global invariant logic.
* **Examples**: Stocks, Gas Station, Jump Game.
* **Detailed Guide**: [Intro: Optimazing Greedy Algo using Logical Invariant](greedy_with_invariant.md), [Advanced: Greedy Algo Using Multiple Invariants](greedy_with_multi_constraint.md)

## 2. Constructive / Parsing Greedy (Validity)

* **Goal**: Build a valid construction or translation.
* **Invariant**: The current prefix interpretation is logically sound and follows the rules (grammar).
 **Logic**: Every local step preserves global invariant logic.
* **Examples**: Roman to Integer, Integer to Roman.
* **Detailed Guide**: [Constructive Greedy Algorithm](greedy_with_invariant.md)

---

### The "Look-Ahead" Rule (+1)

In many Greedy problems, the **Local Decision** requires a peek at the next state to preserve the invariant:

- **Roman to Integer**: Peek `i + 1` to see if current is negative.
- **Gas Station**: We don't peek `i + 1` in the code, but the logic "forces" us to start fresh from `i + 1` if the invariant is violated.
