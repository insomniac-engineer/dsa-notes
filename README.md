<div align="center">

# 🧠 Open DSA Pattern Handbook

*Quick recall system for acing the coding interviews*

![LeetCode Progress](https://img.shields.io/badge/LeetCode_Progress-46%2F150_%2830%25%29-orange?style=for-the-badge&logo=leetcode)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-June%202026-blue?style=for-the-badge&logo=calendar)](https://github.com/yuliiachimyrys/dsa-notes)
[![Language](https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge&logo=python)](https://python.org)

</div>

---

## 👋 Hi

I'm Yuliia (yuchi). This repository is a **quick recall system** for the **[Top 150 LeetCode problems](https://leetcode.com/studyplan/top-interview-150/)**.

Like most developers, I seek growth opportunities in my career. That said, I have to keep my Leetcode skills on a decent level to ace the algo interview.

Over time, I learnt that strong algorithmic performance is not about memorization but about **inductive thinking**. This is an iterative process that happens throughout the entire journey of interview prepping.

When solving problems, I focus on:

- recognizing the **signals** that hint at a specific pattern
- maintaining the correct **invariants**
- and building an intuition for why a solution works

This repository is where I collect those notes - something I (or anyone) can revisit right before the interview.

FAQ:
<details>
<summary><b>What programming language to use for DSA?</b></summary>

TL;DR: Python.

Since university I used Java, but I made a strategic move to Python in 2025 for the technical interviews. When time is the most critical constraint, Python allows to bypass the boilerplate and focus 100% on logic rather than syntax.

UPD: I started to collect some syntax pitfalls into python_notes file in the repo.
Rabbit hole of turning human language into programming one is endless! (I still google most of the stuff)

</details>

<details>

<summary><b>Does the order of solving LC problems matter?</b></summary>

Yes. I pay attention to pattern taxonomy first.

  My workflow:

  1. Identify the signal (e.g., "Sorted array" + "Find a pair").
  2. Select the pattern (e.g., "Two Pointers").
  3. Establish the invariant (e.g., "Left pointer only moves right").
  4. Draft pseudocode to verify logic.
  5. Implement in Python to finalize.

</details>
<details>
<summary><b>How do you sync LC solutions to GitHub?</b></summary>

It's auto-synced using [LeetHub-3.0](https://github.com/QasimWani/LeetHub) browser extension.

</details>
<details>
<summary><b>How do you automate your pattern taxonomy?</b></summary>
As most of the developers, I hate to CTRL+C and CTRL+V all the same data between notes and folders. My personal belief, if anything is done twice - I automate it. Check the automate section below or just run script locally:

```python3
python3 scripts/update_taxonomy.py --dry-run
```

</details>
<details>

<summary><b>Other references</b></summary>

1. Python Distilled by David M. Beazley

While you can google most of the stuff when it comes to syntax, I do enjoy to see all the data in one single paper edition, so I can re-visit it.

</details>
---

## 🏗 Repository Architecture

## 📁 `/patterns/`

The **Strategic Layer**. Contains the "why" and "how":

- **The Signal**: When to use this pattern.
- **The Template**: Reusable Python boilerplate.
- **The Invariant**: Critical logic that must hold true.
- **Common pitfalls**: Mistakes to avoid

## 📁 `/problems/`

The **Implementation Layer**. Contains clean, optimal Python solutions mapped to their specific pattern.

---

## How To Use This Repository?

This repository is designed as a pre-interview refresher, not a full algorithm textbook.

Suggested workflow:

1. Review Pattern Taxonomy & Cheat Sheet to refresh recognition signals
2. Revisit Pattern READMEs to recall invariants and templates
3. Skim solved problems

---

## 🧭 **Pattern Signals**

Use this table during the first minute of pattern recognition.

| If the problem asks for... | Try this Pattern... | Key Intuition | Signals |
| :--- | :--- | :--- | :--- |
| **In-place array modification** | Read / Write Compression | **One-way (Fast/Slow)**: One pointer scans, the other writes valid data. | Remove element, Remove duplicates, Filter, In-place |
| **Pair matching in sorted data** | Classic Two Pointers | **Two-way (Left/Right)**: Typically **sorted** input. Pointers move toward each other to find a target. | Sorted, Target Sum, Palindrome, Pairs |
| **Min/max in subarray** | Sliding window | Expand window to satisfy condition, **shrink** to restore validity. Maintain running state instead of recomputing. | Subarray, Substring, Longest/Shortest, At most / At least |
| **Finding a majority element (Boyer-Moore)** | Voting / Cancellation | Cancel out competing values to reveal dominant candidate. | Majority, > N/2, Count |
| **Local optimum for global best** | Greedy Optimization | Global feasibility check. Take the best step now without looking back. Define local invariant to preserve global one | Is solution feasible, max/min profit |
| **Design Dict: $O(1)$ lookup + $O(1)$ random** | Use dict + list for random synchronously | Store values in list, track indices in dictionary. Sync them. | GetRandom O(1), Constant Time, Design Dict |
| **Design Stack: $O(1)$ get min** | Use list + list for min synchronously | Use additional list for storing min values. Sync them. | GetMin O(1), Constant Time, Design Stack |
| **Consecutive numbers** | Sliding index | Start at i, use sliding index while nums[i] + 1 == nums [i + 1]. Find all ranges with +1 difference. Keep track of the start of range to format output | Ranges, intervals |
| **Intervals Overlaps** | Sort intervals by start | Compare current start with previous end | Overlap, Meetings, Intervals, Merge |
| **Non-overlapping intervals** | Sort intervals by end | Longer interval has wider range, therefore we can't get rid of smaller intervals by picking an arrow number | Min number of arrows to burst balloons |
| **Simplify Path** | Split string and use stack for O(1) del/adding elements | **path.split("/")** for splitting; to return string with delimiter back **"/" + "/".join(stack)** | Simplify Path, UNIX-style file system |
| **Valid Parentheses** | Use stack | Use stack for adding enclosing characters. E.g. '{' would match to '}' in stack. | Open/closing brackets, parentheses, matching |
| **Valid Anagram** | Dict for chars counters | Pythonic way: Counter(s) == Counter(t) | Rearranging letters, permutation |
| **Top k elements** | Min heap for O(nlogk) | Pythonic way: heapq.heappush/pop() | Top K elements |

---

## 🧩 **Pattern Taxonomy**

I struggled a lot through my journey to understand the patterns. In the end, what helped me is to creat my own short WIKIs - happy to share them here.

### **Documented Patterns**

| Pattern Category | Signature Problems | Notes (if any) |
|:-----------------|:-------------------|:----------|
| **Arrays & Hashing** | [0217 Contains Duplicate](problems/0217-contains-duplicate/) • [0242 Valid Anagram](problems/0242-valid-anagram/) • [0001 Two Sum](problems/0001-two-sum/) | [🚧 Coming soon](patterns/two_pointers) |
| **Stack** | 👥 [0150 Evaluate Reverse Polish Notation](problems/0150-evaluate-reverse-polish-notation/) • 👥 [0224 Basic Calculator](problems/0224-basic-calculator/) • [0020 Valid Parentheses](problems/0020-valid-parentheses/) • [0071 Simplify Path](problems/0071-simplify-path/) | [📚 WIKI: Stack](https://www.hellointerview.com/learn/code/stack/overview) • [📚 WIKI: Monotonic Stack](https://www.hellointerview.com/learn/code/stack/monotonic-stack) |
| **Intervals** | [0228 Summary Ranges](problems/0228-summary-ranges/) • [0252 Meeting Rooms](problems/0252-meeting-rooms/) • [0057 Insert Interval](problems/0057-insert-interval/) • [0452 Minimum Number Of Arrows To Burst Balloons](problems/0452-minimum-number-of-arrows-to-burst-balloons/) | [📚 WIKI: Intervals](patterns/intervals) |
| **Sliding Window** | [0209 Minimum Size Subarray Sum](problems/0209-minimum-size-subarray-sum/) • [Longest Substring Without Repeating Characters](problems/0003-longest-substring-without-repeating-characters/) | [📚 WIKI: Sliding Window](patterns/sliding_window.md) |
| **Greedy - Optimization** | [Gas Station](problems/0134-gas-station/) • [Best Time to Buy/Sell Stock](problems/0121-best-time-to-buy-and-sell-stock/) • [Best Time to Buy/Sell Stock II](problems/0122-best-time-to-buy-and-sell-stock-ii/) • [Jump Game](problems/0055-jump-game/) • [Jump Game II](problems/0045-jump-game-ii/) • [Assign Cookies](problems/0455-assign-cookies/) | [📚 WIKI: Greedy](patterns/greedy/README.md) |
| **Greedy – Construction** | [Roman to Integer](problems/0013-roman-to-integer/)| [📚 WIKI: Greedy](patterns/greedy/README.md)|
| **Fast/Slow Pointers** | [Remove Element](problems/0027-remove-element/) • [Remove Duplicates I](problems/0026-remove-duplicates-from-sorted-array/) • [Remove Duplicates II](problems/0080-remove-duplicates-from-sorted-array-ii/) | [📚 WIKI: Read/Write Compression (Fast/Slow Pointers)](patterns/two_pointers/read_write_compression.md) |
| **Classic Two Pointers** | [Merge Sorted Array](problems/0088-merge-sorted-array/) • [Valid Palindrome](problems/0125-valid-palindrome/) • [Is Subsequence](problems/0392-is-subsequence/) • [Two Sum II](problems/0167-two-sum-ii-input-array-is-sorted/) • [0015 3Sum](problems/0015-3sum/) | [📚 WIKI: Classic Two Pointers](patterns/two_pointers/classic_two_pointers.md) |
| **Voting / Cancellation (Boyer-Moore)** | [Majority Element](problems/0169-majority-element/) | [📚 WIKI: Boyer-Moore Voting](patterns/boyer_moore_voting.md) |
| **Design** | 👥 [Insert Delete GetRandom O(1)](problems/0380-insert-delete-getrandom-o1/) • [0155 Min Stack](problems/0155-min-stack/) | [📚 WIKI: Design DS Problems](patterns/design_problems.md) |
| **In-Place Swap** | [Rotate Array](problems/0189-rotate-array/) | [📚 WIKI: In-Place Swap](patterns/in_place_swap.md) |
| **Array / String** | [Longest Common Prefix](problems/0014-longest-common-prefix/) | - |

---

## 🤖 Automation

This repository uses a small automation pipeline to keep the pattern taxonomy in sync.
When a new problem is added with `pattern:` metadata in its README,  a GitHub Action automatically updates the taxonomy table.

This ensures the repository remains consistent and free from manual bookkeeping.

You can preview changes locally using:

```bash
python3 scripts/update_taxonomy.py --dry-run
```

---

<div align="center">

### **💬 Let's Connect!**

Constructive feedback and collaboration opportunities are always welcome!

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/yuliia-chimyrys-software-engineer001/)

</div>

<!---LeetCode Topics Start-->
# LeetCode Topics

## Hash Table

| Problem Name | Difficulty |
| ------- | ------- |
| [0205-isomorphic-strings](https://github.com/chilya-coder/dsa-notes/tree/main/0205-isomorphic-strings/) | Easy |

## String

| Problem Name | Difficulty |
| ------- | ------- |
| [0020-valid-parentheses](https://github.com/chilya-coder/dsa-notes/tree/main/0020-valid-parentheses/) | Easy |
| [0071-simplify-path](https://github.com/chilya-coder/dsa-notes/tree/main/0071-simplify-path/) | Medium |
| [0205-isomorphic-strings](https://github.com/chilya-coder/dsa-notes/tree/main/0205-isomorphic-strings/) | Easy |

## Stack

| Problem Name | Difficulty |
| ------- | ------- |
| [0020-valid-parentheses](https://github.com/chilya-coder/dsa-notes/tree/main/0020-valid-parentheses/) | Easy |
| [0071-simplify-path](https://github.com/chilya-coder/dsa-notes/tree/main/0071-simplify-path/) | Medium |
| [0150-evaluate-reverse-polish-notation](https://github.com/chilya-coder/dsa-notes/tree/main/0150-evaluate-reverse-polish-notation/) | Medium |
| [0155-min-stack](https://github.com/chilya-coder/dsa-notes/tree/main/0155-min-stack/) | Medium |

## Design

| Problem Name | Difficulty |
| ------- | ------- |
| [0155-min-stack](https://github.com/chilya-coder/dsa-notes/tree/main/0155-min-stack/) | Medium |

## Array

| Problem Name | Difficulty |
| ------- | ------- |
| [0150-evaluate-reverse-polish-notation](https://github.com/chilya-coder/dsa-notes/tree/main/0150-evaluate-reverse-polish-notation/) | Medium |

## Math

| Problem Name | Difficulty |
| ------- | ------- |
| [0150-evaluate-reverse-polish-notation](https://github.com/chilya-coder/dsa-notes/tree/main/0150-evaluate-reverse-polish-notation/) | Medium |
<!---LeetCode Topics End-->