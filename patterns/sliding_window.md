# Sliding Window General
1. Keep naming simple

```
sliding_window -> too long
seen -> good
```
2. ```for r in range(len(s))``` canonical loop
3. ```while r - l + 1 > k``` canonical invariant for shrinking
4. We typically move only l+=1 if window exceeds. r is incremented (scans) automatically.
---
## LC examples
[121. Best Time to Buy and Sell Stock](../problems/0121-best-time-to-buy-and-sell-stock/)

```python
1.  buyPrice = min(buyPrice, i)
2.  profit = max(profit, i - buyPrice)
```

[3. Longest Substring Without Repeating Characters](../problems/0003-longest-substring-without-repeating-characters/)

1. Move l only when there's a duplicate in char sequence

  ```python3
        for r in range(len(s)):
            while s[r] in uniq:
                uniq.remove(s[l])
                l += 1
```

[424. Longest Repeating Character Replacement](../problems/0424-longest-repeating-character-replacement/)

1. Keep dict to check the most common char in word
2. On each iteration check if there are enough replecement for other than most common character values in sliding window
3. Update dict (most common char) when you move l pointer

```python
    while (r - l + 1) - max_count > k:
        char_count[s[l]] -= 1
        l += 1
```

[567. Permutation in String](../problems/0567-permutation-in-string/)

Naive brute force approach:

Since it's permutation - we care about frequences, use defaultdict(int).

1) Dict for pattern s1, dict for seen
2) Traverse through s2, compare pattern and seen (takes O(26*n))
3) Shrink when seen window is bigger than pattern one, decrease dict value, if it equals 0 - remove it

```python
    while (r - l + 1) > len(s1):
        seen[s2[l]] -= 1

        if seen[s2[l]] == 0:
            del seen[s2[l]]
        l += 1
```

Dict comparison of English lowercase takes O(n * 26)

```python
            # This comparison takes 26 chars to compare
            if pattern == seen:
                return True
```

**Optimized approach:**
Time Complexity: O(n)

Instead of comparing 2 dicts - maintain 2 variables **need and have**.

```python
need, have = len(s1), 0
```

1. Increase have only when the **frequencies** are matching

```python
    if pattern[s2[r]] == seen[s2[r]]:
        have += 1
```

2. When shrinking window - decrease *have* only if frequency is met (if not - the previous equality check won't work anyways, we don't care)

```python
 while r - l + 1 > len_s1:
    if pattern[s2[l]] == seen[s2[l]]:
        have -= 1
```

3. Now compare not both dicts, but *have and seen* (int values), so we achieve O(n) as the best possible time complexity.