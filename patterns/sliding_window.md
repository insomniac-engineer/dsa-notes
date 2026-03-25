# 🪟 Sliding Window

---

## 💡 Intuition

The Sliding Window pattern maintains a **dynamic subarray (window)** over a sequence, expanding to explore and shrinking to restore validity.

> [!IMPORTANT]
> **No Recomputation:** Instead of recalculating from scratch for every subarray, we maintain a **running state** (sum, frequency map, count) and update it incrementally as the window moves.

---

## 🔑 Key Concepts

### What is the Window?
A **contiguous subarray** defined by two pointers: `left` (start) and `right` (end). The right pointer expands the window; the left pointer shrinks it.

### Why does Sliding Window work?
A sliding window approach is valid when:
1. The problem involves **contiguous subarrays or substrings**.
2. The window state can be updated **incrementally** in $O(1)$ as elements enter/leave.
3. There is a **monotonic relationship** — expanding can only make the condition "more satisfied" (or "more violated"), never oscillating.

### 📋 Types of Sliding Window

| Type | Logic | Behavior |
| :--- | :--- | :--- |
| **Shrinkable (min-length)** | Expand to satisfy condition, **shrink** to find smallest valid window. | `while` loop to shrink once condition is met. |
| **Expandable (max-length)** | Expand as far as possible while condition holds, **shrink** only when violated. | `while` loop to shrink once condition breaks. |

---

## 🎯 Core Principle

Expand `right` to include new elements. When the window satisfies (or violates) a condition, shrink from `left` to optimize.

> [!TIP]
> **Expand → Check → Shrink:** The right pointer always moves forward. The left pointer only moves forward to restore or optimize. This guarantees $O(n)$ total work.

---

## Sliding Window Template

1. **Initialize State**
    * Running total, frequency map, or counter.
2. **Expand Window** (move `right`)
    * Add `arr[right]` to the running state.
3. **Shrink Window** (move `left`)
    * While condition is met/violated → update result, remove `arr[left]` from state, advance `left`.
4. **Return Result**

```python
def sliding_window(arr):
    left = 0
    state = ...  # running sum, dict, counter
    result = ...  # min/max/count

    for right in range(len(arr)):
        # Expand: add arr[right] to state
        state = update(state, arr[right])

        # Shrink: while condition is met/violated
        while should_shrink(state):
            result = optimize(result, right - left + 1)
            state = remove(state, arr[left])
            left += 1

    return result
```

---

## 📚 Canonical Examples

---

### 🔍 [Minimum Size Subarray Sum (209)](../../problems/0209-minimum-size-subarray-sum/)

**Problem Pattern:** Find shortest subarray with sum ≥ target (shrinkable window)

**📊 Invariant:**
- `total` = sum of elements in current window `[left..right]`

**🔧 Logical Condition:**
- `total >= target` → window is valid, try to shrink

**⚡ Local Decision:**
- While valid → record length, shrink from left

```python
def minSubArrayLen(target, nums):
    l, total = 0, 0
    res = float('inf')

    for r in range(len(nums)):
        total += nums[r]

        while total >= target:
            res = min(r - l + 1, res)
            total -= nums[l]
            l += 1

    return 0 if res == float('inf') else res
```

---

### 🔍 [Longest Substring Without Repeating Characters (3)](../../problems/0003-longest-substring-without-repeating-characters/)

**Problem Pattern:** Find longest substring with all unique characters (expandable window)

**📊 Invariant:**
- `key_frequency` = set/dict tracking characters in current window

**🔧 Logical Condition:**
- Duplicate detected → window is invalid, must shrink

**⚡ Local Decision:**
- While duplicate exists → remove `s[left]` from set, advance left

```python
def lengthOfLongestSubstring(s):
    key_frequency = {}
    l, r = 0, 0
    res = 0

    while r < len(s):
        while s[r] in key_frequency:
            del key_frequency[s[l]]
            l += 1

        key_frequency[s[r]] = 1
        res = max(res, r - l + 1)
        r += 1

    return res
```

---

## ⚠️ Common Pitfalls

1. **Off-by-one in window size:** Window length is `right - left + 1`, not `right - left`.
2. **Forgetting to update state on shrink:** Every time `left` moves, the removed element must be subtracted from the running state.
3. **Using sliding window on non-contiguous problems:** Sliding window only works for **contiguous** subarrays/substrings. If the problem allows skipping elements, consider two pointers or DP instead.
