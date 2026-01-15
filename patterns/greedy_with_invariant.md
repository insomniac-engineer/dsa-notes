# Greedy Algorithm Using Invariants

Main idea is to make a **locally optimal decision at each step** that leads to a **globally optimal solution**. 

Greedy algorithms **do not backtrack**.
Once a decision is made, it is never revisited.

---

## Core principle

At every step:

- make the best decision given the current state
- without revisiting previous choices

The key insight is that we are **NOT simulating actions**.

Instead, we track as **invariant** that represents the best possible
state or outcome so far.

Invariant examples:
- total gas owned (Gas Station problem)
- total profit (Stock problem)

---

## Data

Greedy solutions usually track:
 
- minimum/maximum
- invariant (total profit/gas owned)

---

## Canonical example

### Best Time to Buy and Sell Stock (121)

Data we track:

- we track the **minimum buy price**
- we track the **profit** (`price today - minBuy`) -> **invariant**

Each iteration local decision:

- update `minBuy` if the current price is lower
- or update `profit` if selling today is more profitable
- or do nothing


### Best Time to Buy and Sell Stock 2 (122)

Data we track:
- **total profit** -> invariant

Each iteration local decision:

- we compare neighboring prices (`i` and `i - 1`)
- if the price increased, we have a guaranteed profit
- add this to total profit

### Gas Station (0134)

**Global feasibility check**
if sum(gas) < sum(cost): return -1
aka: does this task have a solution at all?

Data we track:
- **total owned gas** -> invariant

Each iteration local decision:

- if ownedGas is less than needed to reach next station

Canonical pattern:
```
if sum(gas) < sum(cost): return -1 # our invariant can't be less than total cost

gasOwned = 0
start = 0

for i in range(n):
    gasOwned += gain[i] - loss[i] #we don't simulate any movements, we use invariant
    if gasOwned < 0:
        start = i + 1
        gasOwned = 0
```


<!-- ---

## Greedy Invariant - Farthest Reach (Jump Game problem)

Unlikely with making local optimum solution at EACH step, here we consider a boundary of reachability.

### Key idea

We track **how far we can reach** using **ANY** of the positions processed so far.

At each step, we ask:

> Given all positions in the prefix `[0..i]`,  
> what is the farthest (max) index we can reach?

**before each step check if our "farthest" value is still in range of [0...currentElement]**

--- -->

<!-- **Jump Game (55)**

- `nums[i]` represents the maximum jump length from index `i`
- the goal is to check whether the last index is reachable

We do **not** simulate jumps.
We only verify that each index **lies within the reachable boundary**.

If the boundary reaches or exceeds the last index, the answer is `true`.

```
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthestPoint = 0

        for i in range(len(nums)):
            #check if farthestPoint is still included in range nums[0]...i
            if i > farthestPoint:
                return False
            farthestPoint = max(farthestPoint, i + nums[i])
            if farthestPoint >= len(nums) - 1:
                return True
        return False
``` -->