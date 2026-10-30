# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
DFS 
traverse from the root 
root is always good node 
params - node, max_node 
basecase when reached the end, return 
if good node -> current node > max_node -> increment nonlocal goodnodes return 
dfs 
"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0

        def dfs(node, max_node): 
            if not node: 
                return 
            nonlocal good_nodes 
            if node.val >= max_node:
                max_node = node.val
                good_nodes += 1
            
            dfs(node.left, max_node)
            dfs(node.right, max_node)
            return 
        
        dfs(root, float('-inf'))
        return good_nodes
        