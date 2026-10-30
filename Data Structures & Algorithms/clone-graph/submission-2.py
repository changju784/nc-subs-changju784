"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
DFS 
!!!! always define what recursion function returns
!!!! what's the basecase (when it reaches the end)
recursively add new nodes for each neighbor and set copy of node value to current node 
basecase: if reached end, return None 
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hash_map = {} # key - node, value - copy 
        def DFS(node):
            if node in hash_map: 
                return hash_map[node]

            copy = Node(node.val)
            hash_map[node] = copy
            for neighbor in node.neighbors: 
                copy.neighbors.append(DFS(neighbor))
            return copy

        return DFS(node) if node else None
            

        