# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, curr = None, head
        nxt = None
        while curr:
            nxt = curr.next
            curr.next = prev

            prev = curr
            curr = nxt
        counter = 0
        reversed_head = prev
        if n == 1:
            reversed_head = reversed_head.next
        else:
            while prev:
                counter += 1
                if counter == n - 1:
                    prev.next = prev.next.next
                prev = prev.next

        prev = None
        while reversed_head:
            nxt = reversed_head.next
            reversed_head.next = prev

            prev = reversed_head
            reversed_head = nxt
        return prev