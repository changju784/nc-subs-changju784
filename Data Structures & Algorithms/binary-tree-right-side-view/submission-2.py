# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
BFS 
starting from root, 
we pop the current node out of queue 
if we push right subtree before left to queue, 
first popped queue in each depth will be right most element. 
while queue: 
    for _ in range(len(queue)):
        pop the right most queue 
        check right tree
            push to queue 
        check left tree 
            push to queue 
    push the first popped element in the result. 
[3, 2] 1
[]
"""
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []
        result = [root.val] 
        queue = deque([root])

        while queue: 
            # right_most_val = queue[0].val 
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.right: 
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            if queue: 
                result.append(queue[0].val)
        return result