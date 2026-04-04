# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        qq = deque()
        parents = {}
        qq.append(root)
        while qq:
            node = qq.popleft()
            if node.left:
                qq.append(node.left)
                parents[node.left] = node
            if node.right:
                qq.append(node.right)
                parents[node.right] = node


        p_ancestors = {p}
        start = p
        while root not in p_ancestors:
            p_ancestors.add(parents[start])
            start = parents[start]
        print([pp.val for pp in p_ancestors])

        q_ancestors = {q}
        start = q
        while root not in q_ancestors:
            if parents[start] in p_ancestors:
                return parents[start]
            start = parents[start]
        

        
        

#        - we must find out if p and q are in the root's left or right or the same node
        