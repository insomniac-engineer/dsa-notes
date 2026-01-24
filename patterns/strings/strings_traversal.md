# String traversal concepts in Python

Creating this as a cheatsheet since I'm still learning Python for LeetCode-style problems.

## Traverse from the end

- `s[::-1]` - simple traversal, no index needed
- `range(len(s)-1, -1, -1)` - when index or index-based condition is required
- `while` - most flexible, useful for multi-phase logic

### Using slicing (no index needed)

```python
for ch in s[::-1]:
    ...

```

### Using range (index-aware)

```python
for i in range(len(s)-1, -1, -1):
    ch = s[i]
```

### Using while (most flexible)

```python
i = len(s) - 1
while i >= 0:
    ch = s[i]
    i -= 1
```
