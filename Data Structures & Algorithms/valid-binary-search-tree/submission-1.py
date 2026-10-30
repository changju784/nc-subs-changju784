# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Traverse left and right 
        def DFS(node, low=float('-inf'), high=float('inf')): 
            if not node: 
                return True 
            if not(low < node.val < high):
                return False 
            return DFS(node.left, low, node.val) and DFS(node.right, node.val, high)
        return DFS(root)