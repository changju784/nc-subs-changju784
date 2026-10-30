# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
BST - at most 2 nodes left node smaller than root, right node larger than root 
LCA - common ancester that is lowest in the tree

Key points 
1. We need to mark/memoize LCA so far from traversing 
2. p or q could be ancestor 
3. we can compare root, p, q val 


params curr_node,lca 
if p, q > node -> lca located in right 
if p, q < node -> lca located in left 
if p <= node <= q or q <= node <= p -> curr node is lca return it 

Recursion O(H) O(H) Iteration O(H) O(1)

"""
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root: 
            if root.val < p.val and root.val < q.val: # anscestor located in right
                root = root.right 
            elif root.val > p.val and root.val > q.val: # ancestor located in left 
                root = root.left
            else: 
                return root 
        return None
        

        