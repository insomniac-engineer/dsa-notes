<div align="center">

# 🧠 **Open DSA Pattern Handbook**
### *Quick recall system for acing the coding interviews*

![LeetCode Progress](https://img.shields.io/badge/LeetCode_Progress-42%2F150_%2828%25%29-orange?style=for-the-badge&logo=leetcode)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-April%202026-blue?style=for-the-badge&logo=calendar)](https://github.com/yuliiachimyrys/dsa-notes)
[![Language](https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge&logo=python)](https://python.org)

</div>

---

## 👋 Hi!

I'm Yuliia (Yuchi). This repository is a **quick recall system** for the **[Top 150 LeetCode problems](https://leetcode.com/studyplan/top-interview-150/)**.

Over time, I learned that strong algorithmic performance is not about memorization but about **inductive thinking**. This is an iterative process that happens throughout the entire journey of being a Software Engineer.

When solving problems, I focus on:

- recognizing the **signals** that hint at a specific pattern
- maintaining the correct **invariants**
- and building an intuition for why a solution works

This repository is where I collect those notes.

There are many excellent resources that explain algorithms in depth.

Instead, this repo exists as a fast recall practical system - something I (or anyone) can revisit right before the interview.

FAQ:
<details>
<summary><b>What programming language to use for DSA?</b></summary>

TL;DR: Python.

Since university I sticked with Java, but I made a strategic move to Python in 2025 for the technical interviews. When time is is the most critical constraint, Python allows to bypass the boilerplate and focus 100% on logic rather than syntax.

UPD: I started to collect some syntax pitfalls into python_notes file in the repo.
Rabbit hole of syntax is endless!

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
As most of the developers, I hate CTRL+C and CTRL+V all same data between notes and folders. If anything is done twice - I stick to automate it. Check the automate section below or just run script locally:

```pyhon3
python3 scripts/update_taxonomy.py --dry-run
```

</details>

---

## 🏗 Repository Architecture

### 📁 `/patterns/`
The **Strategic Layer**. Contains the "why" and "how":

- **The Signal**: When to use this pattern.
- **The Template**: Reusable Python boilerplate.
- **The Invariant**: Critical logic that must hold true.
- **Common pitfalls**: Mistakes to avoid

### 📁 `/problems/`
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
| **$O(1)$ lookup + $O(1)$ random** | Dict + List Hybrid | Store values in list, track indices in dictionary. | GetRandom O(1), Constant Time |
| **Consecutive numbers** | Sliding index | Start at i, use sliding index while nums[i] + 1 == nums [i + 1]. Find all ranges with +1 difference. Keep track of the start of range to format output | Ranges, intervals |
| **Intervals Overlaps** | Sort intervals by start | Compare current start with previus end | Overlap, Meetings, Intervals, Merge |
| **Non-overlapping intervals** | Sort intervals by end | Longer interval has wider range, therefore we can't get rid off smaller intervals by picking an arrow number | Min number of arrows to burst balloons |

---

## 🧩 **Pattern Taxonomy**

I struggled a lot through my journey to understand the patterns. In the end, what helped me is to creat my own short WIKIs - happy to share them here.

<div align="center">

### **Documented Patterns**

</div>

| Pattern Category | Signature Problems | Notes (if any) |
|:----------------|:-------------------|:----------|
| **Intervals** | [0228 Summary Ranges](problems/0228-summary-ranges/) • [0252 Meeting Rooms](problems/0252-meeting-rooms/) • [0057 Insert Interval](problems/0057-insert-interval/) • [0452 Minimum Number Of Arrows To Burst Balloons](problems/0452-minimum-number-of-arrows-to-burst-balloons/) | [📚 WIKI: Intervals](patterns/intervals) |
| **Sliding Window** | [0209 Minimum Size Subarray Sum](problems/0209-minimum-size-subarray-sum/) • [Longest Substring Without Repeating Characters](problems/0003-longest-substring-without-repeating-characters/) | [📚 WIKI: Sliding Window](patterns/sliding_window.md) |
| **Greedy - Optimization** | [Gas Station](problems/0134-gas-station/) • [Best Time to Buy/Sell Stock](problems/0121-best-time-to-buy-and-sell-stock/) • [Best Time to Buy/Sell Stock II](problems/0122-best-time-to-buy-and-sell-stock-ii/) • [Jump Game](problems/0055-jump-game/) • [Jump Game II](problems/0045-jump-game-ii/) • [Assign Cookies](problems/0455-assign-cookies/) | [📚 WIKI: Greedy](patterns/greedy/README.md) |
| **Greedy – Construction** | [Roman to Integer](problems/0013-roman-to-integer/)| [📚 WIKI: Greedy](patterns/greedy/README.md)|
| **Fast/Slow Pointers** | [Remove Element](problems/0027-remove-element/) • [Remove Duplicates I](problems/0026-remove-duplicates-from-sorted-array/) • [Remove Duplicates II](problems/0080-remove-duplicates-from-sorted-array-ii/) | [📚 WIKI: Read/Write Compression (Fast/Slow Pointers)](patterns/two_pointers/read_write_compression.md) |
| **Classic Two Pointers** | [Merge Sorted Array](problems/0088-merge-sorted-array/) • [Valid Palindrome](problems/0125-valid-palindrome/) • [Is Subsequence](problems/0392-is-subsequence/) • [Two Sum II](problems/0167-two-sum-ii-input-array-is-sorted/) • [0015 3Sum](problems/0015-3sum/) | [📚 WIKI: Classic Two Pointers](patterns/two_pointers/classic_two_pointers.md) |
| **Voting / Cancellation (Boyer-Moore)** | [Majority Element](problems/0169-majority-element/) | [📚 WIKI: Boyer-Moore Voting](patterns/boyer_moore_voting.md) |
| **Dict + List Hybrid** | [Insert Delete GetRandom O(1)](problems/0380-insert-delete-getrandom-o1/) | [📚 WIKI: Dict + List](patterns/dict_list_random_access.md) |
| **In-Place Swap** | [Rotate Array](problems/0189-rotate-array/) | [📚 WIKI: In-Place Swap](patterns/in_place_swap.md) |

---

## 🤖 Automation

This repository uses a small automation pipeline to keep the pattern taxonomy in sync.

Whenever a new problem is added with `pattern:` metadata in its README,  a GitHub Action automatically updates the taxonomy table.

This ensures the repository remains:

- Consistent
- Self-maintaining
- Free from manual bookkeeping

You can preview changes locally using:

```bash
python3 scripts/update_taxonomy.py --dry-run
```

---

<div align="center">

### **💬 Let's Connect!**

Constructive feedback and collaboration opportunities are always welcome!

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/yuliia-chimyrys-software-engineer001/)