# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # DFS Sol:

        res = []

        def dfs(node, depth):
            if not node: # base case
                return None
            if depth == len(res): # this is the first node at this depth
                res.append(node.val) # only append the first right side childe we see
            # recurse on the right side first, then left
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root, 0)
        return res

            