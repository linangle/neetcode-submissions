# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case
        if not root:
            return 0
        
        # DFS recursion
        # add 1 for each new "root" we process, + 1 for the initial
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        
