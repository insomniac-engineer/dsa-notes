# Optimizing Greedy Algorithm

----

## Intuition

The main idea is to make a **locally optimal decision at each step** that preserves **global optimality**.

Greedy algorithms **do not backtrack**.
Once a decision is made, it is never revisited.

The correctness of greedy algorithm relies on maintaining an invariant.

----

### What is Invariant?

An **invariant** is a logical state on some property that must remain true throughout the algorithm.

### Why Greedy works?

Greedy is correct if:

1. A local decision preserves the invariant
2. The invariant guarantees global optimality

----

### Types of Greedy Invariants

* **Greedy with a single invariant**
-> a single tracked state defines optimality
-> the invariant can be maintained during one traversal
-> if the invariant is violated, the current prefix is discarded

* **Greedy with multiple invariants**
-> multiple independent constraints
-> each constraint introduces its own bound
-> the final solution must satisfy all invariants simultaneously

----

### Core Principle

At every step:

* make the best decision given the current state
* never revisit previous choices

The key insight - we are **NOT simulating actions**.

Instead, we track an **invariant** - a **logical property** that represents the best possible achievable state so far.

### Invariant vs Invariant Condition

Invariant:

```
gasOwned = remaining gas if we start from the candidate station
```

Invariant Condition:
```python
gasOwned >= 0
```
----

## 🛠️ Common Greedy Algorithm Template

### 🔄 Step-by-Step Approach

#### 1️⃣ **Global Feasibility Check** *(optional)*
> 🎯 **Question:** Does a solution exist at all?

- Common in LeetCode when problem states "return -1 if impossible"
- Check global constraints before attempting local optimization

```python
# Example: Gas Station
if sum(gas) < sum(cost):
    return -1  # Impossible to complete circuit
```

#### 2️⃣ **Define State Variables**
> 🎯 **Question:** What data do we need to track?

Common state types:
- `min/max` - extrema tracking
- `balance/total` - cumulative values
- `prefix/suffix` - partial results

#### 3️⃣ **Identify Core Invariant**
> 🎯 **Question:** What logical property must remain true?

```python
# Examples:
gasBalance    # remaining fuel
maxProfit     # best profit so far
minPrice      # lowest price seen
```

#### 4️⃣ **Define Invariant Condition**
> 🎯 **Question:** When is the invariant satisfied?

```python
# Examples:
gasBalance >= 0     # route is feasible
profit >= 0         # no losses allowed
balance > threshold # constraint satisfied
```

#### 5️⃣ **Maintain Invariant During Traversal**
> 🎯 **Question:** How do we preserve the invariant at each step?

```python
for element in input:
    # Update state
    state += process(element)
    
    # Check invariant violation
    if not invariant_satisfied(state):
        # Reset or adjust strategy
        reset_state()
```

---

## Canonical Examples

### 📈 [Best Time to Buy and Sell Stock (121)](../../problems/0121-best-time-to-buy-and-sell-stock/)

**Problem Pattern:** Single-pass profit optimization

**📊 Invariants:**
- `minBuy` = minimum price seen so far
- `maxProfit` = best achievable profit in processed prefix

**⚡ Local Decisions:**
- Update `minBuy` if current price is lower
- Update `maxProfit` if selling today yields better profit
- Continue scanning

```python
def maxProfit(prices):
    minBuy = float('inf')
    maxProfit = 0
    
    for price in prices:
        minBuy = min(minBuy, price)
        maxProfit = max(maxProfit, price - minBuy)
    
    return maxProfit
```

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
