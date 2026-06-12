# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper: 
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val # return true if self is less than other

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # HEAP SOLUTION
        # idea : instead of scanning all heads every time, use a min-heap 
        if len(lists) == 0: # base case
            return None
        
        res = ListNode(0) # dummy node
        cur = res
        minHeap = []

        for lst in lists:
            if lst is not None:
                heapq.heappush(minHeap, NodeWrapper(lst))
        
        while minHeap:
            node_wrapper = heapq.heappop(minHeap) # pop the minimum
            cur.next = node_wrapper.node # attach this node to cur.next
            cur = cur.next # move cur forward

            if node_wrapper.node.next: # if the minimum has a next node, push it onto the heap
                heapq.heappush(minHeap, NodeWrapper(node_wrapper.node.next))

        return res.next # exclude the dummy