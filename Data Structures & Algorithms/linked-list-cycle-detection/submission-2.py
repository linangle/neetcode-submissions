# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        # next.() retrieves subsequent item from an iterator
        # if the fast pointers do not exist, they reached null
            # --> no cycles
        while fast and fast.next: # remember we shift fast by 2 on each iteration --> fast.next() must also exist
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False 