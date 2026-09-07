"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        oldToCopy = {None:None}

        curr = head

        # old value w next and random -> new value with value
        # Node(3,next=7,rndm=None) -> Node(3)
        # Node(7,next=4,rndm=None) -> Node(7)
        while curr:
            # pass any val to Node
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
        curr = head

        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next
        return oldToCopy[head]