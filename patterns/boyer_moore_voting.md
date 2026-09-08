# Voting / Cancellation Pattern (Boyer–Moore)

Used to find a dominant element by canceling out different values.

## When to use
- Majority element (> n/2)
- Guaranteed existence of dominant candidate
- Need O(1) space

## Core idea
- Keep a candidate and a counter
- Same value → counter++
- Different value → counter--
- When counter == 0 → choose new candidate

## Why it works
A majority element cannot be fully canceled by minority elements.

## Complexity
- Time: O(n)
- Space: O(1)

## Classic problems
- [Majority Element](../problems/0169-majority-element/)

## Canonical implementation
```python
candidate = None
count = 0
for x in nums:
    if count == 0:
        candidate = x
    count += 1 if x == candidate else -1
