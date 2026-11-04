# General Notes

0. Python basics first, otherwise it's a rabit hole of both syntax + task logic
1. Big O (Time/Space Complexity) and define it each time for each problem
2. Focus on 4 built-in types and know when to use each: lists, tuples, sets and dicts
3. Always ask "why"?

## Arrays (Lists) Notes

1. Array is a contiguous block of memory.
2. 2 pointers pattern is often used; dict/set/heap are often used as DS
3. Variables readability, ```seen``` is better than ```temp```
4. Is data **sorted?** -> (commonly 2 pointers)
5. Distance between r and l pointers: ```r - l + 1```
6. Dict keys are always **HASHABLE** (tuple/str/int/frozenset). It means you have to transform non-hashable DS into hashable one in order to store it in dict.
7. ```range(0, len(nums))``` -> last element is EXCLUSIVE [0, len(nums))
8. ```sort(nums)``` changes permanently in-place, ```sorted()``` will return
9. If we have 2d array:
   - it's an array of arrays
   - to traverse rows -> outer loop sets the row, inner loop traverses elements in it
   - to traverse columns -> outer loop sets the column ```range(0, len(nums))```, inner loop to traverses rows with that column
10. Typically there are couple of solutions per each task. The "right" answer is the one that works optimally. 
    For e.g. [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/description/) could be solved in $O(N$)$ by
    - using dict [val] -> index
    - sliding window to shrink to k

11. Scalability: Check if we could convert input to set. If the input is big and indices don't really play a role - we can skip duplicates first to reduce TC, for e.g. [9. Longest Consecutive Sequence](../../problems/0128-longest-consecutive-sequence/0128-longest-consecutive-sequence.py)

---

## Set Notes

1. S = {20, 'Jessa', 35.75}
2. s = set()
3. Mutable itself
4. Unordered
5. Unique
6. Contains immutable (hashable) data types

---

# Dict Notes

1. defauldict() - creates key-val pair automatically instead of throwing KeyError
2. {}, dict() - throws KeyError if key is not present

---


### [1. Contains Duplicate](../../problems/0217-contains-duplicate/0217-contains-duplicate.py)

0. Intuition: Set can't contain duplicates
1. Short Pythonic way:

```python
    return len(nums) != len(set(nums))
```

---

### [2. Valid Anagram](../../problems/0242-valid-anagram/0242-valid-anagram.py)

0. Intution: Anagram is a **permutation** of characters. To check if words are anagrams, all their chars frequencies must be the same. We use dict to calculate chars frequencies.
1. Edge Case: `if len(s) != len(t): return False`. Anagrams MUST have the same length.
2. Short Pythonic way (can mention on interview, but they will ask to implement exact aglo)

    ```python
    Counter(s) == Counter(t)
    ```

4. Invariant:

```python
            if char_t not in s_map or s_map[char_t] < 0:
                return False
```

5. Delete key-value from dict when there is no more char occurance

```python
            if dict_s[char_t] == 0:
                del dict_s[char_t]
```
---

### [3. Two Sum](../../problems/0001-two-sum/0001-two-sum.py)

0. Intution: value1 + (target - value1) = sum
1. Create a ```dict[val] -> index``` and check if the complementary value (`target - val`) already exists in dict on each iteration.
2. If Sorted: we could use the **2 pointers** approach and optimize Space Complexity to O(1)

---

### [4. Group Anagrams](../../problems/0049-group-anagrams/0049-group-anagrams.py)

0. Intution: words should grouped by same pattern - frequencies of all chars must be the same.

**Approach #1: by sorting $O(n logn)$**

1. Create dict `{word_pattern -> word1, word2}`
2. Add sorted word to dict
Caveat:
`sorted(str)` returns a sorted **list**. 
Dict keys MUST be **hashable** (immutable). We CANNOT use lists as keys.
    * *Approach 1 (Tuple):* `tuple(sorted(s))`
    * *Approach 2 (String):* `''.join(sorted(s))`

**Approach #2: counter for each character position O(N)** (most intuitive and optimized)

```python
    freq_counter = [0] * 26
    pattern_words = defaultdict(list)
    for s in strs:
        freq_counter = [0] * 26
        for ch in s:
            freq_counter[ord(ch) - ord('a')] += 1 # key must be hashable
        pattern_words[tuple(freq_counter)].append(s)
    return list(pattern_words.values())
```

### [5. Top K Frequent Elements](../../problems/0347-top-k-frequent-elements/0347-top-k-frequent-elements.py)

0. Intuition: We have val-frequencies pairs and we need to limit to k results. So we use min heap (balanced binary tree). This tree has always min value as the root. On each iteration, we push value and check if the length of tree is more than k - then element with loweset frequency (root) is pushed out.

1. Initalize val_freq dict
2. Intialize min_heap
3. Push (freq, val) to min_heap
4. Invariant - result len must be always k
5. Time Complexity: $O(N log k)$, where k is how many elements are processed in heap
6. Space Complexity $O(N + k)$, n - elements in dict, k - in heap

```python
        my_dict = Counter(nums)
        heap = []

        for val, freq in my_dict.items():
            # first push, otherwise wrong freq could be popped
            heapq.heappush(heap, (freq, val))
            if len(heap) > k:
                heapq.heappush(heap)
        # return values using list comprehension
        return [val for _, val in heap]
```

### [6. Encode and Decode Strings](../../problems/premium-encode-decode-strings/encode-decode-strings.py)

0. Intuition: since any character can appear inside of each word, we seperate each by counter of word and "#".
Important: think ahead how we parsevalue, "5#" is much easier to parse then "#5".

Pattern: ```25#Hello2#Hi```

## [7. Products of Array Except Self](../../problems/0238-product-of-array-except-self/0238-product-of-array-except-self.py)

0. Intuition: prefix/postfix approach (imo unintuitive problem at all)

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

### [8. Valid Sudoku](../../problems/0036-valid-sudoku/0036-valid-sudoku.py)

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

### [9. Longest Consecutive Sequence](../../problems/0128-longest-consecutive-sequence/0128-longest-consecutive-sequence.py)

0. Use for loop since the input order is chaotic (idx doesn't matter)
1. **IMPORTANT! We could have 2GB input full of duplicates**, so first **convert input to set**. Traverse this set.
2. Start element is when ```i - 1``` in nums_set doesn't exist
3. Maintain streak variable to find max streak
// 3. To return distance -> substract j - i -> end_point - start_point - optional, IMO can be easily messed up during interview to count i/j.

### [10. Missing Number](https://github.com/insomniac-engineer/leetcode-dump/blob/main/0268-missing-number/0268-missing-number.py)

Instead of sorting $O(nlogn)$ and comparing index == cur_val, simply return expected_sum - actual $O(n)$

```python
        expected_sum = sum(range(len(nums) + 1))
        actual_sum = sum(nums)
        return expected_sum - actual_sum
```

### [15. 3Sum](https://leetcode.com/problems/3sum/description/)

0. Intuition: it's the same 2 pointers problem with tweak.
e.g. [-1,0,1,2,-1,-4]
[ -4 -1 -1 0 1 2] - sorted list
      l.       r