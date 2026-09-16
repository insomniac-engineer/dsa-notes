# General Notes

0. Beginner advice - separate Python syntax from task logic first (aka pseudocode first).
1. **Is data sorted?**
2. **Visualization:**
3. **Lookup Time Complexity:**
    * `list`: $O(n)$
    * `set`, `dict`: $O(1)$
4. **Distance = r - l + 1**
5. Dict keys **HASHABLE** (tuple/string)

---

## [1. Contains Duplicate](../../problems/0217-contains-duplicate/0217-contains-duplicate.py)

1. We use a `set` to filter duplicates, taking $O(n)$ time to traverse all elements.
2. If Sorted: we could use the **2 pointers** approach and optimize Space Complexity to $O(1)$.
3. Pythonic way:

```python
    return len(nums) != len(set(nums))
```

---

## [2. Valid Anagram](../../problems/0242-valid-anagram/0242-valid-anagram.py)

1. Edge Case: `if len(s) != len(t): return False`. Anagrams MUST have the same length.
2. Anagram is a **permutation** of characters (char frequencies must be the same).
3. Pythonic way to count:

    ```python
    Counter(s) == Counter(t)
    ```

4. Invariant: char must be always present in dict and its frequency > 0

```python
            if char_t not in s_map or s_map[char_t] == 0:
                return False
```

---

## [3. Two Sum](../../problems/0001-two-sum/0001-two-sum.py)

1. Create a `dict` (`val -> index`) and check if the complementary value (`target - val`) exists on each iteration. Time: $O(n)$.
2. If Sorted: we could use the **2 pointers** approach and optimize Space Complexity to $O(1)$.

---

## [4. Group Anagrams](../../problems/0049-group-anagrams/README.md)

1. Create a `{word_pattern -> list(strs)}` dict and group anagrams together.
2. The word_pattern (dict key) must be sorted.
3. `sorted(str)` returns a sorted **list**. 
4. Dict keys MUST be **hashable** (immutable). We CANNOT use lists as keys.
    * *Approach 1 (Tuple):* `tuple(sorted(s))`
    * *Approach 2 (String):* `''.join(sorted(s))`

5. Advanced Optimization ($O(L)$ instead of $O(L \log L)$):

    We can replace word sorting with a fixed-size frequency array.

    ```python
    # Creates a list of 26 zeros: [0, 0, ..., 0]
    count = [0] * 26 
    
    for char in word:
        # Maps character ASCII code to index 0-25
        count[ord(char) - ord('a')] += 1
        
    key = tuple(count) # Tuples are hashable!
    ```

    > **How it works:** 
    > There are 26 lowercase English characters. `ord()` returns the ASCII code.
    > * `ord('a')` $\rightarrow$ 97
    > * `ord('b')` $\rightarrow$ 98
    > * `'d'`: `ord('d') - ord('a')` $\rightarrow$ $100 - 97 = 3$

## [5. Top K Frequent Elements](../../problems/0347-top-k-frequent-elements/0347-top-k-frequent-elements.py)

1. Dict for calculating frequencies
2. Traverse through dict, add to heap (balanced binary tree)
3. Invariant - len of heap must be less than k, if it's more - pop
4. Time Complexity: $O(n log k)$, where k is how many elements are processed in heap
5. Space Complexity $O(n + k)$, n - elements in dict, k - in heap

```python
        my_dict = Counter(nums)
        heap = []

        for val, freq in my_dict.items():
            # pushing by frequencies
            heapq.heappush(heap, (freq, val))
            if len(heap) > k:
                heapq.heappop(heap)
        # return values using list comprehension
        return [val for _, val in heap]
```

## [6. Encode and Decode Strings](../../problems/premium-encode-decode-strings/encode-decode-strings.py)

1. Pattern: ```25#Hello2#Hi```, use ```counter#``` as the delimeter (for 2+ digits values)
2. To decode digit:

```python
    digit = 0
    while s[i] != '#':
        digit *= 10 
        digit += int(s[i])
        i += 1
```

3. Pythonic way: ```word = s[i : i + end_pos]``` instead of a while loop to get the word from start pos to the end one

## [7. Products of Array Except Self](../../problems/0238-product-of-array-except-self/0238-product-of-array-except-self.py)

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        # 1 2 4 6

        # 1 1 2  8  48
        #  48 48 24 6  1

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res
```

## [8. Valid Sudoku](../../problems/0036-valid-sudoku/0036-valid-sudoku.py)

1. Keep defaultdicts (auto handle KeyError) for col, row and sub-boxes uniqueness

    ```python
    col = defaultdict(set) # idx_col -> set()
    row = defaultdict(set) # idx_row -> set()
    boxes = defaultdict(set) # (idx_box_col, idx_box,row) -> set()
    ```

2. To traverse through List[List[str]]

    ```python
    for idx_r, board_row in enumerate(board):
        for idx_c, val in enumerate(board_row):
    ```

3. For checking boxes (3x3) use ```boxes[(idx_r // 3, idx_c // 3)]```

## [9. Longest Consecutive Sequence](../../problems/0128-longest-consecutive-sequence/0128-longest-consecutive-sequence.py)

0. Use for loop since the input order is chaotic (idx doesn't matter)
1. IMPORTANT! We could have 2GB input full of duplicates, so first **convert input to set**. Traverse this set.
2. Start element is when ```i - 1``` in nums_set doesn't exist
3. Maintain streak variable to find max streak
// 3. To return distance -> substract j - i -> end_point - start_point - optional, IMO can be easily messed up during interview to count i/j.
