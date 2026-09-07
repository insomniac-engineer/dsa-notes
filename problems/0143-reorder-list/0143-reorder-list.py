# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # 1. Find middle using slow/fast approach
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. Reverse the second half
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 3. Merge the two halves
        start = head
        while start and prev:
            nxt1 = start.next
            nxt2 = prev.next

            start.next = prev
            prev.next = nxt1

            start = nxt1
            prev = nxt2