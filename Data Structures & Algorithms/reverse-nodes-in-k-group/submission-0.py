# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # dummy points to the head
        groupPrev = dummy  # groupPrev is the node just before the current group

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth: # if there are less than k elements left, we can't make a group
                break
            groupNext = kth.next # first node after the current group
            
            prev, curr = kth.next, groupPrev.next # reverse prev and curr
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next


    def getKth(self, curr, k): # find the kth node from previous group
        while curr and k > 0: # increment the current forwards k times
            curr = curr.next
            k -= 1
        return curr
            
