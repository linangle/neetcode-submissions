# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and
                    self.sameTree(root.right, subRoot.right))
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base case:
        if not subRoot: # if the subroot is empty, always a subroot of the root
            return True

        if not root: # if the root doesn't exist, the subroot is not a subroot of anything (unless subroot also empty)
            return False
        
        if self.sameTree(root, subRoot): # this is the situation where they are identical
            return True
        
        # recurse over the left and right subtrees
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))
        
        
                    
        