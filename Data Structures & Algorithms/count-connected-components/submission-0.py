"""
edges represent undirected connection 
we can build a graph by hashmap source -> target, target -> source 
we can iterate from 0 to n:
    run DFS recursion 
    parameter: node 
    basecase: when this node not in the graph return none
"""
from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for source, target in edges: 
            graph[source].append(target)
            graph[target].append(source)
        visited = set()

        def dfs(i):
            if i in visited: 
                return 
            visited.add(i)
            for nxt in graph[i]:
                dfs(nxt)

        num_connection = 0
        for i in range(n):
            if i not in visited: 
                dfs(i)
                num_connection += 1
        return num_connection 

