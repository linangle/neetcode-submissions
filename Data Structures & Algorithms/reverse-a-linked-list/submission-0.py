# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # assume no cycles, ends at Null (None)
        prev, curr = None, head
        while curr:
            nxt = curr.next # saves the original next value in the iteration
            # update the curr.next to the previous (to reverse the list)
            curr.next = prev # reversing the pointer
            # update the previous value to be the current
            prev = curr
            curr = nxt # update the current to process the original next value
        # previous pointer updated to be the new head
        return prev

            