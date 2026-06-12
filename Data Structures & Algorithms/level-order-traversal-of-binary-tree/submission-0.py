# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # DFS SOL : O(n) time and space
        # idea : visit the tree level by level, from top to bottom, recursing 
        res = []

        def dfs(node, depth):
            if not node: # base case
                return None
            if len(res) == depth: # if res has no list for this depth, append a new empty list
                res.append([])
            
            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return res