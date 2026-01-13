# Insert Delete GetRandom O(1)

Link to the LC problem: https://leetcode.com/problems/insert-delete-getrandom-o1/

TL;DR: Design a set-like data structure where:

insert(val) -> O(1)
remove(val) -> O(1)
getRandom() -> O(1)

## Logic
The main idea of such problems is deep understanding of core data types operations efficiency.

* dict: insert, delete, lookup by key -> O(1); **random operation is absent**
* list: random operation is present O(1); **but** insert, delete (from middle) -> O(n); insert from end, delete from end -> O(1); insert by index -> O(1); 


No single built-in data structure supports all required operations in O(1).

### Solution

Split responsibilities across two data structures and keep them synchronized.

1) dict: for insert, delete O(1)
2) set: for random O(1) 

**IMPORTANT!**

Since we are using 2 DS in parallel, we need to make sure we **synchronize** them.

For example:

self.dict = {val0:index0, val1:index1, val2:index2}ß
self.list = [val0, val1, val2]


If we want to remove val1 we need:
1) remove it from dict O(1)
2) and also from list. Since removing by i1 is O(n), we grab the last element val2 and overwrite it instead val1. Then pop val2
3) UPDATE INDEX of val2 in dict