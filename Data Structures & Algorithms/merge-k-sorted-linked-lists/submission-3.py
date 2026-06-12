# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # DIVIDE & CONQUER SOLUTION
        # idea : split list of linked lists into halves and recursively merge the left and right halfs into a sorted list --> merge
        if not lists: # base case
            return None
        return self.divide(lists, 0, len(lists) - 1)

    def divide(self, lists, l, r): # l is the left half, r is the right half
        if l > r:
            return None
        if l == r: # only one list to return
            return lists[l]
        # compute the midpoint and recursively divide
        mid = (l + r) // 2
        left = self.divide(lists, l, mid)
        right = self.divide(lists, mid + 1, r)

        return self.conquer(left, right)
        
    # merge left and right using the standard merge two sorted linked lists 
    def conquer(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val: 
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next 
            tail = tail.next
        
        if l1:
            tail.next = l1
        else:
            tail.next = l2
        
        return dummy.next # exclude the dummy

        