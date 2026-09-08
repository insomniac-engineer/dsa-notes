<div align="center">

# 🧠 Open DSA Pattern Handbook

*Quick recall system for acing the coding interviews*

![LeetCode Progress](https://img.shields.io/badge/LeetCode_Progress-46%2F150_%2830%25%29-orange?style=for-the-badge&logo=leetcode)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-August%202026-blue?style=for-the-badge&logo=calendar)](https://github.com/yuliiachimyrys/dsa-notes)
[![Language](https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge&logo=python)](https://python.org)

</div>

----
This repository is a **quick recall system** for the **[Neetcode 150 LC](https://leetcode.com/problem-list/plakya4j//)** - something I (or anyone) can revisit right before the interview.

I struggled A LOT when it came to DSA interviews. My first approach was to memorize the solution, but after a couple of days I couldn't re-write it. That's what led me to realization - strong algorithmic performance is not about memorization, but **inductive thinking**, ability to recognize signals to **patterns** and state clear **invariants**.

FAQ:
<details>
<summary><b>What programming language to use for DSA?</b></summary>

Python. It allows to bypass the boilerplate and focus 100% on logic rather than syntax.

</details>

<details>
<summary><b>How do you sync LC solutions to GitHub?</b></summary>

Auto-synced using [LeetHub-3.0](https://github.com/QasimWani/LeetHub) to dump repo, then copied manually here to avoid sync noise.

</details>
<details>
<summary><b>How do you automate your pattern taxonomy?</b></summary>
Pipeline automation

```bash
python3 scripts/update_taxonomy.py --dry-run
python3 scripts/update_taxonomy.py
```

</details>
----

## 🏗 Repository Architecture

## 📁 `/patterns/`

The **Strategic Layer**. Source of WIKIs. Contains all the "what"s and "why"s.

## 📁 `/problems/`

The **Implementation Layer**. Clean, optimal Python solutions with time/space complexity.

## 📁 `/python_notes/`

The **Syntax Pitfalls**. My own collection of Python syntax pitfalls.

----

## 🧭 **Pattern Signals**

| If the problem asks for... | Try this Pattern... | Key Intuition | Signals |
| :--- | :--- | :--- | :--- |
| **In-place array modification** | Read / Write Compression | **One-way (Fast/Slow)**: One pointer scans, the other writes valid data. | Remove element, Remove duplicates, Filter, In-place |
| **Pair matching in sorted data** | Classic Two Pointers | **Two-way (Left/Right)**: Typically **sorted** input. Pointers move toward each other to find a target. | Sorted, Target Sum, Palindrome, Pairs |
| **Min/max in subarray** | Sliding window | Expand window unconditionally with r pointer. While condition is breaking - **shrink** with left. Pythonic way:  for r in range(len(s)): | Subarray, Substring, Longest/Shortest, At most / At least, k |
| **Finding a majority element (Boyer-Moore)** | Voting / Cancellation | Cancel out competing values to reveal dominant candidate. | Majority, > N/2, Count |
| **Local optimum for global best** | Greedy Optimization | Global feasibility check. Take the best step now without looking back. Define local invariant to preserve global one | Is solution feasible, max/min profit |
| **Design Dict: $O(1)$ lookup + $O(1)$ random** | Use dict + list for random synchronously | Store values in list, track indices in dictionary. Sync them. | GetRandom O(1), Constant Time, Design Dict |
| **Design Stack: $O(1)$ get min** | Use list + list for min synchronously | Use additional list for storing min values. Sync them. | GetMin O(1), Constant Time, Design Stack |
| **Consecutive numbers** | Sliding index | Start at i, use sliding index while nums[i] + 1 == nums [i + 1]. Find all ranges with +1 difference. Keep track of the start of range to format output | Ranges, intervals |
| **Intervals Overlaps** | Sort intervals by start | Compare current start with previous end | Overlap, Meetings, Intervals, Merge |
| **Non-overlapping intervals** | Sort intervals by end | Longer interval has wider range, therefore we can't get rid of smaller intervals by picking an arrow number | Min number of arrows to burst balloons |
| **Simplify Path** | Split string and use stack for O(1) del/adding elements | **path.split("/")** for splitting; to return string with delimiter back **"/" + "/".join(stack)** | Simplify Path, UNIX-style file system |
| **Valid Parentheses** | Use stack | Use stack for adding enclosing characters. E.g. '{' would match to '}' in stack. | Open/closing brackets, parentheses, matching |
| **Valid Anagram** | Chars frequency should be equal | Pythonic way: Counter(s) == Counter(t) | Rearranging letters, permutation |
| **Top k elements** | Use (min) heap for sort | Pythonic way: heapq.heappush(heap, (freq, key)); heapq.heappop(heap) | Top K elements |
| **Longest sequence** | Set for filtering duplicates | Filter duplicates. Start element is the one that doesn't have precessor (x-1). Traverse using FOR loop (input order is chaotic) | Count sequence |
| **Next Greater** | Monotonic Stack | Prefill empty array. Monotonic stack holds indices of smaller values; pop when top element in stack is smaller than incoming one | Daily temperatures |
| **Car Fleet** | Reverse Sorting | cars_sorted = sorted(zip(position, speed), reverse = True). Fleet happens when time > max_time | 853. Car Fleet |

---

## 🧩 **Pattern Taxonomy**

### **Documented Patterns**

| Pattern Category | Signature Problems | WIKI |
|:-----------------|:-------------------|:----------|
| **Arrays & Hashing** | [0217 Contains Duplicate](problems/0217-contains-duplicate/) • [0242 Valid Anagram](problems/0242-valid-anagram/) • [0001 Two Sum](problems/0001-two-sum/) • [0049 Group Anagrams](problems/0049-group-anagrams/) • [0347 Top K Frequent Elements](problems/0347-top-k-frequent-elements/) • [Premium Encode Decode Strings](problems/premium-encode-decode-strings/) • [0238 Product Of Array Except Self](problems/0238-product-of-array-except-self/) • [0036 Valid Sudoku](problems/0036-valid-sudoku/) • [0125 Valid Palindrome](problems/0125-valid-palindrome/) • [0128 Longest Consecutive Sequence](problems/0128-longest-consecutive-sequence/) • [1422 Maximum Score After Splitting A String](problems/1422-maximum-score-after-splitting-a-string/) | [📚 Arrays & Hashing](patterns/arrays_and_hashing/README.md) |
| **Two Pointers** | **Fast/Slow Pointers:**<br>[Remove Element](problems/0027-remove-element/) • [Remove Duplicates I](problems/0026-remove-duplicates-from-sorted-array/) • [Remove Duplicates II](problems/0080-remove-duplicates-from-sorted-array-ii/)<br><br>**Classic (Opposite Directions):**<br>[Merge Sorted Array](problems/0088-merge-sorted-array/) • [Valid Palindrome](problems/0125-valid-palindrome/) • [Is Subsequence](problems/0392-is-subsequence/) • [Two Sum II](problems/0167-two-sum-ii-input-array-is-sorted/) • [0015 3Sum](problems/0015-3sum/) • [0011 Container With Most Water](problems/0011-container-with-most-water/) | [📚 Fast/Slow Pointers](patterns/two_pointers/fast_slow_pointers.md)<br><br>[📚 Classic Two Pointers](patterns/two_pointers/classic_two_pointers.md) |
| **Stack** | [0020 Valid Parentheses](problems/0020-valid-parentheses/)• [0155 Min Stack](problems/0155-min-stack/) • [0150 Evaluate Reverse Polish Notation](problems/0150-evaluate-reverse-polish-notation/) • [0739 Daily Temperatures](problems/0739-daily-temperatures/) • [0224 Basic Calculator](problems/0224-basic-calculator/) • [0071 Simplify Path](problems/0071-simplify-path/) • [0853 Car Fleet](problems/0853-car-fleet/)|<br><br>[📚 Stack](patterns/stack/stack.md) |
| **Sliding Window** | [Best Time to Buy/Sell Stock](problems/0121-best-time-to-buy-and-sell-stock/) • [0209 Minimum Size Subarray Sum](problems/0209-minimum-size-subarray-sum/) • [0003 Longest Substring Without Repeating Characters](problems/0003-longest-substring-without-repeating-characters/) • [0424 Longest Repeating Character Replacement](problems/0424-longest-repeating-character-replacement/) • [0567 Permutation In String](problems/0567-permutation-in-string/) | [📚 WIKI: Sliding Window](patterns/sliding_window.md) |
| **Linked List** | [0141 Linked List Cycle](problems/0141-linked-list-cycle/) • [0021 Merge Two Sorted Lists](problems/0021-merge-two-sorted-lists/) • [0206 Reverse Linked List](problems/0206-reverse-linked-list/) | [🚧 Coming soon](patterns/two_pointers) |
| **Intervals** | [0228 Summary Ranges](problems/0228-summary-ranges/) • [0252 Meeting Rooms](problems/0252-meeting-rooms/) • [0057 Insert Interval](problems/0057-insert-interval/) • [0452 Minimum Number Of Arrows To Burst Balloons](problems/0452-minimum-number-of-arrows-to-burst-balloons/) | [📚 WIKI: Intervals](patterns/intervals) |
| **Greedy - Optimization** | [Gas Station](problems/0134-gas-station/) • [Best Time to Buy/Sell Stock II](problems/0122-best-time-to-buy-and-sell-stock-ii/) • [Jump Game](problems/0055-jump-game/) • [Jump Game II](problems/0045-jump-game-ii/) • [Assign Cookies](problems/0455-assign-cookies/) | [📚 WIKI: Greedy](patterns/greedy/README.md) |
| **Greedy – Construction** | [Roman to Integer](problems/0013-roman-to-integer/)| [📚 WIKI: Greedy](patterns/greedy/README.md)|
| **Voting / Cancellation (Boyer-Moore)** | [Majority Element](problems/0169-majority-element/) | [📚 WIKI: Boyer-Moore Voting](patterns/boyer_moore_voting.md) |
| **Design** | 👥 [Insert Delete GetRandom O(1)](problems/0380-insert-delete-getrandom-o1/) • [0155 Min Stack](problems/0155-min-stack/) | [📚 WIKI: Design DS Problems](patterns/design_problems.md) |
| **In-Place Swap** | [Rotate Array](problems/0189-rotate-array/) | [📚 WIKI: In-Place Swap](patterns/in_place_swap.md) |
| **Array / String** | [Longest Common Prefix](problems/0014-longest-common-prefix/) | - |

---

## 🤖 Automation
Runs automatically on repo pipeline.
Use dry run locally.

```bash
python3 scripts/update_taxonomy.py --dry-run
python3 scripts/update_taxonomy.py
```

---

<div align="center">

### **💬 Let's Connect!**

Constructive feedback and collaboration opportunities are always welcome!

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/yuliia-chimyrys-software-engineer001/)

</div>
