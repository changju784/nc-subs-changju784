# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def DFS(p_node, q_node):
            # check current node exist and compare values.
            if not p_node and not q_node: 
                return True 
            else: 
                if (not p_node and q_node) or (not q_node and p_node):
                    return False 
                if p_node and q_node: 
                    if p_node.val != q_node.val: 
                        return False 
                    return DFS(p_node.left, q_node.left) and DFS(p_node.right, q_node.right)
        return DFS(p, q)


            