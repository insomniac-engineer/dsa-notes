# Design Problems

Most of the design problems, such as:

* Min Stack (https://leetcode.com/problems/min-stack/?envType=study-plan-v2&envId=top-interview-150)
* Insert Delete GetRandom O(1) (https://leetcode.com/problems/insert-delete-getrandom-o1/description/?envType=study-plan-v2&envId=top-interview-150)

Require maintaining 2 data structures with different responsibilities in order to solve problems in O(1) time.
The important part is - we have to update both of them during each iteration.

## Insert Delete GetRandom O(1)

LC link: https://leetcode.com/problems/insert-delete-getrandom-o1/

TL;DR: Design a set-like data structure where:

insert(val) -> O(1)
remove(val) -> O(1)
getRandom() -> O(1)

### Logic

* dict: insert, delete, lookup by key -> O(1); **random operation is absent**
* list: random operation is present O(1); **but** insert, delete (from middle) -> O(n); insert from end, delete from end -> O(1); insert by index -> O(1);

No single built-in data structure supports all required operations in O(1).

### Solution

Split responsibilities across two data structures and keep them synchronized.

1) dict: for insert, delete O(1)
2) set: for random O(1)

**IMPORTANT!**

Both dict and set have to be **synchronized**.

For example:

self.dict = {val0:index0, val1:index1, val2:index2}
self.list = [val0, val1, val2]

If we want to remove val1 we need:

1) remove it from dict O(1)
2) and also from list. Since removing element from list takes O(n), instead of removing we grab the last element (val2) and overwrite val1. Then pop last element in list (val2) with O(1).
3) UPDATE INDEX of val2 in dict (no longer last one)