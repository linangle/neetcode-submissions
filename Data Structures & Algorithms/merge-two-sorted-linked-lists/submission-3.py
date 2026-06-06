# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node (common tech to avoid edge cases)
        dummy = ListNode()
        tail = dummy

        while list1 and list2: # while these both exist, we have to compare
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next 
            else: # if they're equal or list1 is greater, next node is list2
                tail.next = list2   
                list2 = list2.next
            tail = tail.next # move forward to keep rewriting the lists
        
        if list1: # if we run out of l2 and only have l1 left, append the rest of l1
            tail.next = list1
        elif list2: 
            tail.next = list2

        return dummy.next