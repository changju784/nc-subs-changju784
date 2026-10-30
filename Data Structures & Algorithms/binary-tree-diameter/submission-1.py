# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Key Points 
1. Diameter is sum of max height of left and right subtree. 

"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = float('-inf')
        def dfs(node):
            if not node:
                return 0
            nonlocal max_diameter
            left = dfs(node.left)
            right = dfs(node.right)
            max_diameter = max(max_diameter, left + right)
            return 1 + max(left, right)
        dfs(root)
        return max_diameter
        
            