# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        # The Shark Intuition: 
        # We need a function that tells us two things:
        # 1. How deep is this subtree?
        # 2. Who is the "parent" of the deepest nodes in this subtree?
        
        def dfs(node):
            if not node:
                return 0, None
            
            l_depth, l_node = dfs(node.left)
            r_depth, r_node = dfs(node.right)
            
            # If left and right have the same depth, then 'node' is 
            # the common ancestor for all deepest nodes found so far.
            if l_depth == r_depth:
                return l_depth + 1, node
            
            # If one side is deeper, the answer must be in that side.
            if l_depth > r_depth:
                return l_depth + 1, l_node
            else:
                return r_depth + 1, r_node
        
        # We only care about the second part of the result (the node)
        return dfs(root)[1]