# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # ITERATIVE SOL : 
        # idea : iteratively choose the smallest value out of the lists
        res = ListNode(0) # create a dummy node to build from
        cur = res

        while True:
            minNode = -1
            for i in range(len(lists)):
                if not lists[i]: # if the list is empty
                    continue # skip to the next one
                if minNode == -1 or lists[minNode].val > lists[i].val: # if we are starting or we found a new minimum
                    minNode = i
            
            if minNode == -1:
                break
            cur.next = lists[minNode]
            lists[minNode] = lists[minNode].next
            cur = cur.next
    
        return res.next