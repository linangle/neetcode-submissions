# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # MERGING ONE BY ONE
        # idea : merge list 0 and 1 and get a sorted list --> merge that resultant with list 2 ...
            # compare the heads, attach the smaller one, move that list's pointer forward, continue until empty

        if len(lists) == 0: # base case
            return None
        
        for i in range(1, len(lists)):
            lists[i] = self.mergeList(lists[i - 1], lists[i])
        
        return lists[-1]
    
    def mergeList(self, l1, l2):
        dummy = ListNode() # dummy node to make result
        tail = dummy

        while l1 and l2: 
            if l1.val < l2.val: # find the smaller
                tail.next = l1 # append the smaller
                l1 = l1.next # move the smaller's pointer
            else: # if l2 has the smaller or they're equal, do the same thing
                tail.next = l2
                l2 = l2.next
            tail = tail.next 
        if l1: # if we've depleted l2 but l1 still exists, append the entire l1
            tail.next = l1
        if l2: # same concept as above
            tail.next = l2
        return dummy.next # remember we don't include the dummy

