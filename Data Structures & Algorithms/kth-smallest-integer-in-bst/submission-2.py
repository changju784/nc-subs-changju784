# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Traverse the tree either DFS or BFS 
Store nums in maxheap -> keep heap size as k 

Inorder BST traversal 
since tree is BST -- where smaller nodes are stored in left subtree, viceversa. 
Inorder -> left -> current -> right 
Base case: if node reaches end return none 
recurse left first
then if we found count gets k return that node called from left.  
recurse right 

"""

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0 
        def inorderTraverse(node): 
            nonlocal count 
            if not node: 
                return None
            
            left = inorderTraverse(node.left)
            if left is not None: 
                return left 
            
            count += 1 
            if count == k: 
                return node.val 

            right = inorderTraverse(node.right)
            return right

        result = inorderTraverse(root)
        return result