# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # RECURSION SOL : O(h) time, O(h) space
        if not root or not p or not q: # base cases
            return None
        if (max(p.val, q.val)) < root.val: # if both are in the left subtree
            return self.lowestCommonAncestor(root.left, p, q) # recurse on left
        elif (min(p.val, q.val)) > root.val: # if both are in the right subtree
            return self.lowestCommonAncestor(root.right, p, q) # recurse on the right
        else:
            return root # if they're in different subtrees, the root is the LCA
