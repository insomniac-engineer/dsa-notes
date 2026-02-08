<div align="center">

# 🧠 **Open DSA Pattern Handbook**
### *Quick recall system for acing the coding interviews*

[![Progress](https://img.shields.io/badge/Progress-23%2F150-brightgreen?style=for-the-badge&logo=leetcode)](https://leetcode.com/studyplan/top-interview-150/)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-Feb%202026-blue?style=for-the-badge&logo=calendar)](https://github.com/yuliiachimyrys/dsa-notes)
[![Language](https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge&logo=python)](https://python.org)

</div>

---

## 👋 Hi!

I'm Yuliia (Yuchi). This repository is a **quick recall system** for the **[Top 150 LeetCode problems](https://leetcode.com/studyplan/top-interview-150/)**.

Over time, I learned that strong algorithmic performance is rarely about memorizing solutions.
The goal isn't memorization - it's **inductive thinking**. I focus on recognizing the "signals" that trigger specific **patterns** and maintaining the **invariants** required to solve them under time pressure.

There are many excellent resources that provide deep theoretical understanding of algorithms.
Instead, this repo exists as a **quick recall system** - something that can be revisited just before interviews.

<details>
<summary><b>What programming language to use for DSA?</b></summary>
Having spent years of trying mastering DSA with Java, I made a strategic move (following a "hard realization") to Python in 2025 for the technical interviews. I've found that when time is the most critical constraint, Python’s minimalist syntax acts like a multiplier rather than blocker. It allows to bypass the boilerplate and focus 100% on logic rather than syntax.
</details>

<details>
<summary><b>Does the order of solving LC problems matter?</b></summary>
Yes. While Top 150 LC provides raw material, main thing is to pay attention to pattern taxonomy (which I tried to come up in this repo) and solve problems not in ad-hoc way, but categorized.

  My recommended workflow:

  1. Identify the signal (e.g., "Sorted array" + "Find a pair").
  2. Select the pattern (e.g., "Two Pointers").
  3. Establish the invariant (e.g., "Left pointer only moves right").
  4. Draft pseudocode to verify logic.

Implement in Python to finalize.
</details>

---

## 🎯 **Mission & Philosophy**

Build a **fast pattern-based recall system** where:
- Every problem is mapped to a reusable **Mental Model**.
- Solutions prioritize **Interview Practicality** over academic theory.
- We focus on the **Invariant**: the truth that remains constant throughout the algorithm.

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

## 🧭 **Pattern Selection Cheat Sheet**

Use this table during the first minute of pattern recognition.

| If the problem asks for... | Try this Pattern... | Key Intuition | Signals |
| :--- | :--- | :--- | :--- |
| **In-place array modification** | Read / Write Compression | One-way (Fast/Slow): One pointer scans, the other writes valid data. | Remove, Duplicates, Filter, In-place |
| **Pair matching in sorted data** | Classic Two Pointers | Two-way (Left/Right): Pointers move toward each other to find a target. | Sorted, Target Sum, Palindrome, Pairs |
| **Finding a majority element (Boyer-Moore)** | Voting / Cancellation | Cancel out competing values to reveal dominant candidate. | Majority, > N/2, Count |
| **Local optimum for global best** | Greedy Optimization | Immediate Best: Take the best step now without looking back. | Max Profit, Jump, Minimum Chips |
| **$O(1)$ lookup + $O(1)$ random** | Dict + List Hybrid | Store values in list, track indices in dictionary. | GetRandom O(1), Constant Time |

---

## 🧩 **Pattern Taxonomy**

<div align="center">

### **🏆 Documented Patterns**

</div>

| Pattern Category | Core Principle | Signature Problems | Notes |
|:----------------|:---------------|:-------------------|:----------|
| **Greedy – Optimization** | Local best choice → Global result | [Gas Station](problems/0134-gas-station/) • [Best Time to Buy/Sell Stock](problems/0121-best-time-to-buy-and-sell-stock/) • [Best Time to Buy/Sell Stock II](problems/0122-best-time-to-buy-and-sell-stock-ii/) • [Jump Game](problems/0055-jump-game/) • [Jump Game II](problems/0045-jump-game-ii/) • [Assign Cookies](problems/0455-assign-cookies/) | [📚 Greedy 101](patterns/greedy/README.md) |
| **Greedy – Construction** | Build answer via local rules | [Roman to Integer](problems/0013-roman-to-integer/) • Integer to Roman | [📚 Greedy 101](patterns/greedy/README.md) |
| **Read / Write Compression** | "Filter" elements in-place | [Remove Element](problems/0027-remove-element/) • [Remove Duplicates I](problems/0026-remove-duplicates-from-sorted-array/) • [Remove Duplicates II](problems/0080-remove-duplicates-from-sorted-array-ii/) | [🚧 Coming soon](patterns/two_pointers) |
| **Classic Two Pointers** | Match elements from different ends | [Merge Sorted Array](problems/0088-merge-sorted-array/) • [Valid Palindrome](problems/0125-valid-palindrome/)| [🚧 Coming soon](patterns/two_pointers) |
| **Voting / Cancellation (Boyer-Moore)** | Find dominant element via cancellation | [Majority Element](problems/0169-majority-element/) | [🚧 Coming soon](patterns/boyer_moore_voting.md) |
| **Dict + List Hybrid** | Fast lookup + Random access | [Insert Delete GetRandom O(1)](problems/0380-insert-delete-getrandom-o1/) | [📚 Check dict/set implementation](patterns/dict_list_random_access.md) |


<details>
<summary><b>🔜 Click to view upcoming problems (Backlog)</b></summary>

Rotate Array, H-Index, Product of Array Except Self, Length of Last Word, Longest Common Prefix, Reverse Words in a String, Zigzag Conversion, Find the Index of the First...
</details>

---

## 📊 **Progress Metrics**

<div align="center">

### **📈 Current Status**

```
██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 23/150 (15.3%)

🎯 Target: Top 150 LeetCode Problems
⏱️ Timeline: Active Development  
🔄 Update Frequency: Daily
📅 Last Sync: Feb 7, 2026
```
---

## 🛠️ **Development Workflow**


- **Automated Sync**: [LeetHub-3.0](https://github.com/QasimWani/LeetHub) browser extension
- **Version Control**: Git-based solution tracking
- **Documentation**: Pattern-first approach with detailed analysis
- **Quality Gates**: Code review, complexity analysis, edge case validation

---

## 🤝 **Contributing & Feedback**

<div align="center">

### **💬 Let's Connect!**

Constructive feedback and collaboration opportunities are always welcome!

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/yuliia-chimyrys-software-engineer001/)

</div>
