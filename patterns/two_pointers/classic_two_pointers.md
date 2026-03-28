# Classic Two Pointers

This pattern uses two pointers that move **toward each other**.

---

## Core idea

- **left** pointer starts at the beginning
- **right** pointer starts at the end
- They converge based on a condition (sum comparison, character match, etc.)

Unlike Read/Write Compression, both pointers are **equal citizens** — neither is strictly a "reader" or "writer".

---

## When to use

- Sorted array + target sum/pair matching
- Palindrome checking
- Merging from two sorted sources
- Container / area maximization problems
- Signal words: Sorted, Target Sum, Palindrome, Pairs, Merge

---

## Canonical template

```python
left, right = 0, len(arr) - 1

while left < right:
    if condition(arr[left], arr[right]):
        # found / process
        left += 1
        right -= 1
    elif need_bigger:
        left += 1
    else:
        right -= 1
```

---

## Problems

### [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)

**Reverse Two Pointers** — fill from the **end/tail** to avoid overwriting unprocessed elements.

```
         i
    [5,6,7,0,0,0]
         j
    [1,2,3]
```

Don't forget to merge remaining tail of the second array to the first one.

```
     i
    [0,0,0,5,6,7]
         j
    [1,2,3]
```

Final result after merging remaining tail of nums2:

```
    [1,2,3,5,6,7]
```

### [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

Left and right pointers converge toward the center, skipping non-alphanumeric characters and comparing case-insensitively.

### [392. Is Subsequence](https://leetcode.com/problems/is-subsequence/)

Two pointers on two different strings: one advances on `s`, the other on `t`. When characters match, advance the `s` pointer.

### [167. Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

Sorted array — if sum is too large, move `right` left; if too small, move `left` right.

### [15. 3Sum](https://leetcode.com/problems/3sum/)

Fix one element, then run classic two-pointer on the remaining sorted subarray. Skip duplicates on all three pointer positions.

### [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

Maximize area between two lines. Always move the shorter side inward — moving the taller side can never increase the area.
