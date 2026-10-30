# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
DFS 
what to return inverted nodes 
base case - when reached the end return none 

"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node: 
                return None 
            l, r = node.left, node.right 
            node.left, node.right = r, l 
            dfs(node.left)
            dfs(node.right)
            return node 
        head = root 
        dfs(head)
        return root 