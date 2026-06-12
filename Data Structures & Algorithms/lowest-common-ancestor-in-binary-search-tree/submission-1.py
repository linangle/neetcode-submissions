# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # iteration sol : O(h) time, O(1) space
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val: # both are in the right subtree
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val: # both are in the left subtree
                cur = cur.left
            else: # they're in different subtrees, root is LCA
                return cur