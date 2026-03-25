# Read / Write Compression

This pattern is used for **in-place filtering** of arrays where elements
need to be kept or discarded based on a condition.

---

## Core idea

Two pointers move in the **same direction** (left → right):

- **read pointer** (`j` or `x` in for-each): scans every element
- **write pointer** (`i` or `write`): marks the boundary of valid output

Everything before `write` is the valid result.
Everything at or after `write` is garbage.

```
[ valid region | garbage ]
               ↑
             write
```

---

## When to use

- "Remove element", "Remove duplicates", "Filter in-place"
- The problem requires $O(1)$ extra space
- Input is often (but not always) sorted

---

## Canonical template

```python
write = 0

for x in nums:
    if should_keep(x):
        nums[write] = x
        write += 1

return write
```

---

## Problems

### [27. Remove Element](https://leetcode.com/problems/remove-element/)

One pointer for traversing input, second to fill final list (by the condition `currentValue != val`).

```
[3,2,2,3], val = 3
[2,2,_,_]
```

### [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

`i` — write pointer
`j` — read pointer (one step ahead of write)

Logical invariant: all elements before write should stay unique.

```python
i = 0
j = 1

while j < len(nums):
    if nums[i] != nums[j]:
        i += 1
        nums[i] = nums[j]
    j += 1
return i + 1
```

```
 i j
[0,0,1,1,1,2,2,3,3,4]
[0,1,2,3,4,_,_,_,_,_]
```

### [80. Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

Variation: allow up to `k` duplicates (here `k = 2`).
We only need to check whether the current element equals the element `k` positions before (`nums[write - 2]`).

```
[ valid | garbage ]
        ↑
      write

[0,0,1,1,1,1,2,3,3]
     ↑   ↑   ↑
[0,0,1,1,2,3,3,_,_]
```
