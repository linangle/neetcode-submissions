# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxH (self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxH(root.left), self.maxH(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # largest diameter will be between two leaves
        # sum of a node's left subtree and right subtree heights
        # use DFS to get those subtree heights

        # base case
        if not root:
            return 0
        
        # dfs recursion
        # get each subtree height
        heightL = self.maxH(root.left)
        heightR = self.maxH(root.right)
        # add them to get the diameter
        diameter = heightL + heightR

        # recurse on the subtrees
        sub = max(self.diameterOfBinaryTree(root.left),
                self.diameterOfBinaryTree(root.right))

        return max(diameter, sub)


