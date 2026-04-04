# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, upper_lim, lower_lim):

            if root is None:
                return True

            if root.val >= upper_lim or root.val <= lower_lim:
                return False

            return (dfs(root.left, root.val, lower_lim) and 
                    dfs(root.right, upper_lim, root.val))

        return dfs(root, 1001, -1001)


        
        