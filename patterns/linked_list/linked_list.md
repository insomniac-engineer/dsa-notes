# Linked List

## 3 main patterns

1. **Dummy Node**

Create dummy node, point ref to it.
IMPORTANT: Move ref only.

```python
    dummy = ListNode()
    first = dummy
```

2. **Floyds (Turle/Hare) Algorithm (Slow/Fast pointers)**

Used to detect linked list cycles.
Eventually if there's a cycle fast and slow pointers will meet.

```python
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

3. **Reverse Linked List**

```python
    prev, curr = None, head
    nxt = None

    while curr:
        nxt = curr.next
        curr.next = prev

        prev = curr
        curr = nxt
    return prev
```

### NC150 Problems

[206. Reverse Linked List](../../problems/0206-reverse-linked-list/0206-reverse-linked-list.py)

Standard Reverse Linked List pattern (upper section)

[21. Merge Two Sorted Lists](../../problems/0021-merge-two-sorted-lists/0021-merge-two-sorted-lists.py)

Dummy node with ListNode(0), and tail that points to this node.
Iterate over 2 lists, if value of first one (node) is less, point tail next to it, else - to the second. Move nodes.

**IMPORTANT!** since list1 and list2 has different length, it could be possible that one of them would be shorter than the other.
In this case, check:

```python
        if list1:
            tail.next = list1
        else:
            tail.next = list2
```

[141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/description/)

FLOYD'S ALGO
