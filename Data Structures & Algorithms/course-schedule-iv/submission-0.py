"""
input: integer numCourses, prerequisite [c, prerequisite course], queries 
output: return if each query's prerequisite exists from the original courses 
Directed graph 
[[1,0],[2,1],[3,2]] [0,1]
2 -> 1 -> 0  
|
3

Build adjacency list using hashmap key - course value - list of prerequisites 
DFS for each query[i][0]
for each recursion initialize visit set to prevent cycle 
param - course 
base case - if curr course found in visited set return False 
if curr course is query[i][1] return True 
recurse to all children of curr course 
return False <- not found after running all neighbors
"""
from collections import defaultdict
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # build adj list 
        adj = defaultdict(list)
        for c, p in prerequisites: 
            adj[c].append(p)
        
        def dfs(course, prereq):
            if course in visited: 
                return False 
            if course == prereq: 
                return True 

            visited.add(course)

            for neighbor in adj[course]:
                if dfs(neighbor, prereq): 
                    return True 
            return False 

        
        result = [False] * len(queries)
        for i, q in enumerate(queries):
            visited = set() 
            c, p = q
            result[i] = dfs(c, p)
        
        
        return result 


        