"""
Tree - if it's connected and no cycle 
build a graph by hashtable 
key - source node, value - list of connected nodes 
while we traverse this in each number, starting from 0 to n-1
find if there's cycle. 
To determine the cycle, we can check the visit status of current node 
another hashtable to store the status of visits. 
key - node, value - 0 (not visited) 1 (visiting) 2 (visited) 

DFS O(V*E) O(V*E) V - nodes E - edges
basecase - when we reached the end, 
if current node in visited has status of 1 -> we have a cycle 
if current node in visited has sdtatus of 2 -> no cycle 
mark current node as 1 (visiting)
recursively check the nodes that are connected and see if they have cycle. 
mark current node as 2 (visited)

"""
from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)

        # build a graph that represents connectivity 
        for source, target in edges: 
            graph[source].append(target)
            graph[target].append(source)
        
        visited = set()
        def checkCycle(node, parent):
            if node in visited: # cycle
                return False 

            visited.add(node)
            for child in graph[node]:
                if child == parent: 
                    continue 
                if not checkCycle(child, node):
                    return False 
            return True 
            
        
        if checkCycle(0, -1):
            if len(visited) == n: 
                return True 
        return False 
            

        