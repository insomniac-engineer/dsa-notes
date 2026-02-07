<div align="center">

# 🧠 **Open DSA Pattern Handbook**
### *Quick recall system for acing the coding interviews*

[![Progress](https://img.shields.io/badge/Progress-TBD%2F150-brightgreen?style=for-the-badge&logo=leetcode)](https://leetcode.com/studyplan/top-interview-150/)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-Feb%202026-blue?style=for-the-badge&logo=calendar)](https://github.com/yuliiachimyrys/dsa-notes)
[![Language](https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge&logo=python)](https://python.org)

</div>

---

## 👋 Hi!

I'm Yuliia (Yuchi).

This repository is my personal interview preparation handbook for the **[Top 150 LeetCode problems](https://leetcode.com/studyplan/top-interview-150/)**.

Over time, I learned that strong algorithmic performance is rarely about memorizing solutions.
It's about **inductive** thinking, recognizing **patterns**, maintaining **invariants**, and applying **repeatable mental models** under time pressure.

There are many excellent resources that provide deep theoretical understanding of algorithms.

Instead, this repo exists as a **quick recall system** - something that can be revisited before interviews to refresh pattern recognition and solution intuition.

---

## 🎯 **Mission**

Build a **fast pattern-based recall system** for algorithmic interviews.

### **Core Philosophy**

- Every problem is mapped to a reusable pattern
- Each pattern is documented as a mental model, not an academic theory
- Solutions focus on clarity, correctness, and interview practicality

---

## 🏗 Repository Architecture

### 📁 `/patterns/` - Strategic Layer
The conceptual foundation behind problem solving.

Contains:

- pattern itself, mental model and intuition
- algorithmic templates
- complexity analysis and trade-offs
- common pitfalls and edge cases

---

### 📁 `/problems/` — Implementation Layer
Hands-on application of patterns.

Contains:
- clean and optimal solutions
- edge case handling

---

## How To Use This Repository?

This repository is designed as a pre-interview refresher, not a full algorithm textbook.

Suggested workflow:

1. Review Pattern Taxonomy to refresh recognition signals
2. Revisit Pattern READMEs to recall invariants and templates
3. Skim solved problems to reinforce implementation intuition

Goal: rapid pattern recognition and confident solution decomposition.

---

## 🧩 **Pattern Taxonomy**

<div align="center">

### **🏆 Documented Patterns**

</div>

| Pattern Category | Core Principle | Signature Problems | Notes |
|:----------------|:---------------|:-------------------|:----------|
| **Greedy – Optimization** | Make the best local choice at each step hoping it leads to the best overall result | [Gas Station](problems/0134-gas-station/) • [Best Time to Buy/Sell Stock](problems/0121-best-time-to-buy-and-sell-stock/) • [Best Time to Buy/Sell Stock II](problems/0122-best-time-to-buy-and-sell-stock-ii/) • [Jump Game](problems/0055-jump-game/) • [Jump Game II](problems/0045-jump-game-ii/) • [Assign Cookies](problems/0455-assign-cookies/) | [📚 Greedy 101](patterns/greedy/README.md) |
| **Greedy – Construction** | Build the final answer step-by-step using simple local rules | [Roman to Integer](problems/0013-roman-to-integer/) • Integer to Roman | [📚 Greedy 101](patterns/greedy/README.md) |
| **Read / Write Compression** | Read every element and copy only the valid ones into the front of the array | [Remove Element](problems/0027-remove-element/) • [Remove Duplicates I](problems/0026-remove-duplicates-from-sorted-array/) • [Remove Duplicates II](problems/0080-remove-duplicates-from-sorted-array-ii/) | [📚 TBD](patterns/two_pointers) |
| **Classic Two Pointers** | Use two pointers to compare or match elements from different positions | [Two Sum II](problems/0167-two-sum-ii-input-array-is-sorted/) • [Valid Palindrome](problems/0125-valid-palindrome/) • [Container With Most Water](problems/0011-container-with-most-water/) • [Merge Sorted Array](problems/0088-merge-sorted-array/) | [📚 TBD](patterns/two_pointers) |
| **Voting / Cancellation (Boyer-Moore)** | Find the dominant element by cancelling out different elements | [Majority Element](problems/0169-majority-element/) | [📚 TBD](patterns/boyer_moore_voting.md) |
| **Dict + List Hybrid** | Store elements in both a hash map and list to support fast lookup and random access | [Insert Delete GetRandom O(1)](problems/0380-insert-delete-getrandom-o1/) | [📚 Check dict/set implementation](patterns/dict_list_random_access.md) |

---
🧭 Pattern Selection Cheat Sheet

Remove / filter elements → Read / Write Compression  
Compare or match elements → Classic Two Pointers
Cancel competing values → Voting / Cancellation (Boyer-Moore)
Make best local decision → Greedy Optimization  
Build result step-by-step → Greedy Construction


---

## 📊 **Progress Metrics**

<div align="center">

### **📈 Current Status**

```
██████████████████████░░░░░░░░░░░░░░░░░░ 22/150 (14.7%)

🎯 Target: Top 150 LeetCode Problems
⏱️ Timeline: Active Development  
🔄 Update Frequency: Daily
📅 Last Sync: Feb 6, 2026
```

</div>

<table>
<tr>
<td align="center" width="25%">
<strong>🟢 Easy</strong><br>
<code>12 solved</code>
</td>
<td align="center" width="25%">
<strong>🟡 Medium</strong><br>
<code>8 solved</code>
</td>
<td align="center" width="25%">
<strong>🔴 Hard</strong><br>
<code>2 solved</code>
</td>
<td align="center" width="25%">
<strong>📋 Patterns</strong><br>
<code>5 documented</code>
</td>
</tr>
</table>

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
