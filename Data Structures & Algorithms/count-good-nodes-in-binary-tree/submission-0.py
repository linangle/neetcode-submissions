# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS SOL
        # idea : store a value to track the maximum we've seen so far
            # if node.val >= maxSoFar, it's a good node
        
        def dfs(node, maxVal):
            # base case
            if not node:
                return 0
            
            res = 1 if node.val >= maxVal else 0 
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res
        
        return dfs(root, root.val)
            