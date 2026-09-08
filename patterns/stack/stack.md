Refs:

[HelloInterview: Stack](https://www.hellointerview.com/learn/code/stack/overview)
[HelloInterview: Monotonic Stack](https://www.hellointerview.com/learn/code/stack/monotonic-stack)

----

 [88. Valid Paretheses](https://leetcode.com/problems/valid-parentheses)

![alt text](image-1.png)

1. Valid paretheses can't have only 1 bracket
2. If stack is empty - it means that the parenthesis is broken (no corresponding closing bracket)
3. Optionally - we can add all brackets to map and add values to stack

[155. Min Stack](https://leetcode.com/problems/min-stack/description/)

1. Pop/push/top - O(1) for list
2. getMin requires actual traversing which is O(n)

Solution: one list for pop/push/top, another - updating min for each iteration. When we pop - pop from synced list as well.

```python
    # 1 2 0 stack
    # 1 2 2 sync_stack
```

[150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/)

1. Result is a **SUM** of all operations done
2. .lstrip("-").isdigit() to check negative values
3. Order is important for - and /
4. Result is stack[-1] last element

[739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)