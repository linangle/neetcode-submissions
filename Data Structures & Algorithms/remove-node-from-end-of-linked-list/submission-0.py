# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # initialize a dummy node before the head
        dummy = ListNode(0, head) # set the pointer to the head 
        # initialize pointers to the dummy and n
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1 # once n = 0, we've shifted the right pointer by n

        # shift both pointers until right reaches end of the list
        while right:
            left = left.next
            right = right.next
        
        # nth is the next node from left, delete the node by skipping it
        left.next = left.next.next 

        return dummy.next # don't want to include dummy node
            