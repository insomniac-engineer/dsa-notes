# 📈 Optimizing Greedy Algorithm

---

## 💡 Intuition

The core strategy of a Greedy algorithm is to make a **locally optimal decision at each step** to preserve **global optimality**.

> [!IMPORTANT]
> **No Backtracking:** Once a decision is made, it is never revisited. The correctness of the algorithm relies entirely on maintaining a specific **logical invariant**.

---

## 🔑 Key Concepts

### What is an Invariant?
An **invariant** is a logical property or state that must remain true throughout the execution of the algorithm.

### Why does Greedy work?
A Greedy approach is mathematically sound if:
1. A **local decision** successfully preserves the invariant.
2. The **invariant** itself guarantees the final global optimality.

### 📋 Types of Greedy Invariants

| Type | Logic | Behavior |
| :--- | :--- | :--- |
| **Single Invariant** | A single tracked state defines optimality. | Maintained during one traversal; if violated, the current prefix is discarded. |
| **Multiple Invariants** | Multiple independent constraints or bounds. | The final solution must satisfy all invariants simultaneously. |

---

## 🎯 Core Principle

At every step, we make the best decision based on the current state. 

> [!TIP]
> **Logic over Simulation:** We are **not** simulating actions. Instead, we track an **invariant** - a logical property representing the best possible achievable state so far.

**Example: Gas Station**
* **Invariant:** `gasOwned` (Remaining gas if we start from the candidate station).
* **Condition:** `gasOwned >= 0`.

---

## Greedy Algorithm Template


1. **Global Feasibility Check** *(Optional)*
    * *Goal:* Quick exit if a solution is impossible (e.g., `sum(gas) < sum(cost)`).
2. **Define State Variables**
    * *Common types:* `min/max` (extrema), `balance/total` (cumulative values), `prefix/suffix` (partial results).
3. **Identify Core Invariant**
    * *Question:* What property must stay true? (e.g., `maxProfit`, `minPrice`).
4. **Define Invariant Condition**
    * *Question:* When is the invariant satisfied? (e.g., `balance >= 0`).
5. **Maintain Invariant During Traversal**
    * *Workflow:* Update state $\rightarrow$ Check for violation $\rightarrow$ Reset or adjust strategy.

---

## 📚 Canonical Examples

---

### [Best Time to Buy and Sell Stock II (122)](../../problems/0122-best-time-to-buy-and-sell-stock-ii/)

**Problem Pattern:** Cumulative profit collection

**📊 Invariant:**
- `totalProfit` = accumulated profit from all beneficial transactions

**⚡ Local Decision:**
- If price increased from yesterday → capture the profit
- Otherwise → skip (no transaction)

```python
def maxProfit(prices):
    totalProfit = 0
    
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            totalProfit += prices[i] - prices[i-1]
    
    return totalProfit
```

---

### ⛽ [Gas Station (134)](../../problems/0134-gas-station/)

**Problem Pattern:** Circular array with feasibility constraints

**🎯 Global Feasibility Check:**
```python
if sum(gas) < sum(cost): return -1
```
*If total gas < total cost, no solution exists*

**📊 Invariant:**
- `gasBalance` = net gas if starting from candidate position

**🔧 Logical Condition:**
- `gasBalance >= 0` → current route is feasible

**⚡ Local Decision:**
- If `gasBalance < 0` → discard prefix, restart from next station

```python
def canCompleteCircuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    
    gasBalance = 0
    start = 0
    
    for i in range(len(gas)):
        gasBalance += gas[i] - cost[i]
        
        if gasBalance < 0:  # Invariant violated
            start = i + 1   # Reset starting point
            gasBalance = 0  # Reset balance
    
    return start
```
