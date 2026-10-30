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
        if not root: 
            return []

        queue = deque([root])
        result = []
        depth = 0 

        while queue: 
            # store nodes in current depth
            depth = len(queue)
            nodes = []
            
            for _ in range(depth):
                curr = queue.popleft()
                nodes.append(curr.val)
                # enque left and right 
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            # store current node values in list 
            result.append(nodes)
        return result 
                

        