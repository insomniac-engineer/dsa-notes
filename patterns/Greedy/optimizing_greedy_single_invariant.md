# Optimazing Greedy Algorithm Using Logical Invariant

Main idea is to make a **locally valid decision at each step** that preserves the **global optimality invariant**.

Greedy algorithms **do not backtrack**.
Once a decision is made, it is never revisited.

**Logical invariant** = a logical condition on a tracked property that must remain true throughout the algorithm.

There are 2 types of greedy invariants:

* **Type A (single invariant)**
    - 1 single logical property that fully characterizes optimality
    - invariant can be checked in 1 traversal
    - violation of invariant discards prefix
    - (e.g.: stocks/gas station)


* **Type B  (multi constrant invariant)**:
    - optimality is defined by multiple independent constraints
    - each constraint introduces its own lower bound
    - final solution must satisfy all constraints simultaneously
    - greedy buils minimal bounds, then reconciles them

    - (e.g.: candy/trapping rain water)


Below there's deep dive of single invariant greedy LCs.

---

## Core principle

At every step:

- make the best decision given the current state
- without revisiting previous choices

The key insight is that we are **NOT simulating actions**.

Instead, we track an **invariant** - a **logical property** that represents the best possible state or outcome so far and must remain true after each step.

Typically each invariant has some *logical condition*.

Invariant examples:
- Gas Station: the current gas owned balance *must be non-negative*
- Stock problem: the tracked profit is *optimal for the processed prefix*

Invariant typically appears inside of the traversing cycles.

----
Note:
Invariants are not exclusive to greedy algorithms.
Greedy uses invariants to justify irreversible local choices,
but many linear scans rely on invariants without any choice.

---

## Data

Greedy solutions usually track:
 
- minimum/maximum
- logical invariants (total profit that is optimal for prefix/gas owned that is non-negative)

---

## Algo Cheetsheet

1. **Feasibility check** (only if applicable)

Does solution exist at all?

*usually in LC it clearly states if solution doesn't exist return -1/False -> sign to introduce feasibility check*

2. **Find invariant**

What property/state do we track?

3. **Find logical condition of invariant**

Which logical state of property guarantees that on the current iteration the result is still feasible?

Important!

balance -> itself it's not invariant because it's missing logical condition
balance > 0 -> Bingo!

4. **Traverse input and check on each iteration that logical invariant condition is guaranteed**

---


## Canonical example

### Best Time to Buy and Sell Stock (121)

Data we track:

- we track the **minimum buy price**
- we track the **profit** (`price today - minBuy`) that is optimal -> **logical invariant**

Each iteration local decision:

- update `minBuy` if the current price is lower
- or update `profit` if selling today is more profitable
- or do nothing


### Best Time to Buy and Sell Stock 2 (122)

Data we track:
- **total profit** for the proceeded prefix -> logical invariant

Each iteration local decision:

- we compare neighboring prices (`i` and `i - 1`)
- if the price increased, we have a guaranteed profit
- add this to total profit

### Gas Station (0134)

**Global feasibility check**
*if sum(gas) < sum(cost): return -1*
aka: does this task have a solution at all?

Data we track:
- **total owned gas** -> invariant

Each iteration:

- if the ownedGas (invariant) is violated (balance < 0), discard the prefix

Canonical pattern:
```
*if sum(gas) < sum(cost): return -1* # global feasibility check

gasOwned = 0
start = 0

for i in range(n):
    gasOwned += gain[i] - loss[i] # update state that represents the invariant
    *if gasOwned < 0:* # invariant violation check
        start = i + 1
        gasOwned = 0
```