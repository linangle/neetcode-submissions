# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next: # before we hit the end of the list
            slow = slow.next # slow moves by 1
            fast = fast.next.next # fast moves by 2

        # first node of the second half
        secondhalf = slow.next
        prev = slow.next = None # we're reversing the second half, so start with Null
        while secondhalf:
            tmp = secondhalf.next # store the original variable
            secondhalf.next = prev # reversing
            prev = secondhalf
            secondhalf = tmp
        
        firsthalf, secondhalf = head, prev
        while secondhalf:
            tmp1, tmp2 = firsthalf.next, secondhalf.next
            firsthalf.next = secondhalf
            secondhalf.next = tmp1
            firsthalf, secondhalf = tmp1, tmp2


        