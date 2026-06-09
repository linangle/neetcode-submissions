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
        # SPACE OPTIMIZED I
        # idea: interleave copied nodes inside the original list
        # A --> A' --> B --> B'...
            # A'.random = A.random.next
        # unweave the lists after
        if head is None:
            return None
        
        l1 = head
        while l1 is not None:
            l2 = Node(l1.val) # make the copy
            l2.next = l1.next # original next comes after the copy
            l1.next = l2 # make the pointer from l1 to l1copy
            l1 = l2.next # repeat this process
        
        newHead = head.next

        l1 = head
        while l1 is not None:
            if l1.random is not None: # if the random exists
                l1.next.random = l1.random.next # the copied random is after the original's random
            l1 = l1.next.next 
        
        l1 = head
        while l1 is not None: 
            l2 = l1.next 
            l1.next = l2.next 
            if l2.next is not None:
                l2.next = l2.next.next
            l1 = l1.next

        return newHead
