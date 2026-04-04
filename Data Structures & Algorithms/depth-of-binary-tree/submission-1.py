# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        q = collections.deque()
        depth = 0
        res = 0
        q.append([root, res])

        while q:
            node, res = q.popleft()
            res += 1
            if node.left:
                q.append([node.left, res])
            if node.right:
                q.append([node.right, res])
            if not node.left and not node.right:
                depth = max(depth, res)

        return depth


        

        