# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Binary Tree - node where two children at most 
given binary tree, we want to return nodes in each depth 
BFS - Q 
Starting from queue(source node)
while queue 
    get depth by length of queue 
    for range in depth 
        pop the queue and record current value in same depth
        enqueue left right 
    append current depth nodes to result 

"""
from collections import deque 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        result = [] 
        while queue: 
            level = [] 
            for _ in range(len(queue)): 
                node = queue.popleft()
                if node: 
                    level.append(node.val)
                    if node.left: 
                        queue.append(node.left)
                    if node.right: 
                        queue.append(node.right)
            if level: 
                result.append(level)
        return result