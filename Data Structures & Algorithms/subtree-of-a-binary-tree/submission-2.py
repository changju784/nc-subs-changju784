# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
1. Find the subroot in original Tree 
2. Once we found a subroot, recursively traverse both tree and see the nodes & structures are same. 

1. Recursion to find subtree root from main tree 
base case - if root.val == subroot.val -> return the root 
if root reaches none -> return none 
return either dfs(maintree.left) or dfs(maintree.right)

subroot_in_main = DFS(root)

2. Recursion to check both tree have same nodes and structure 
base case - if their node value are different, return false 
recurse 
return True 

"""
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def findSubRoot(root, subRoot):
            if not root: 
                return False 
            if checkBothTree(root, subRoot): 
                return True 
            return (findSubRoot(root.left, subRoot) or findSubRoot(root.right, subRoot))

        def checkBothTree(main_sub_root, subRoot): 
            if not main_sub_root and not subRoot: 
                return True 
            if not main_sub_root or not subRoot or main_sub_root.val != subRoot.val: 
                return False 
            return checkBothTree(main_sub_root.left, subRoot.left) and checkBothTree(main_sub_root.right, subRoot.right)

        return findSubRoot(root, subRoot)