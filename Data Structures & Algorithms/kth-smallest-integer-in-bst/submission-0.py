# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # recursive sol : O(h + k), O(h) WC O(n)

        cnt = k
        res = root.val

        def dfs(node):
            nonlocal cnt, res # use nonlocal to call a variable outside the function
            if not node: # base case
                return

            dfs(node.left) # go left
            if cnt == 0: # we already found the answer
                return # return early

            cnt -= 1 # decrement count
            if cnt == 0: # this is the k-th smallest
                res = node.val # record the value of the ndoe
                return
            dfs(node.right) # go right if we haven't found the answer yet

        dfs(root)
        return res                      
