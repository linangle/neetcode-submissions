# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxH(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxH(root.left), self.maxH(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        # get the heights of each subtree
        heightL = self.maxH(root.left)
        heightR = self.maxH(root.right)

        # compare the heights
        if abs(heightL - heightR) > 1:
            return False
        
        # recurse on the children
        return self.isBalanced(root.left) and self.isBalanced(root.right)

