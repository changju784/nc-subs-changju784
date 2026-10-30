from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # hashmap to represent graph
        course_graph = defaultdict(list)
        for k, v in prerequisites: 
            course_graph[k].append(v)
        
        # not visited - 0, visiting - 1, vistid - 2 
        visited = [0] * numCourses
        result = []

        def DFS(course): 
            if visited[course] == 1: # Found cycle
                return False
            if visited[course] == 2: 
                return True 
            
            visited[course] = 1 

            for prereq in course_graph[course]: 
                if not DFS(prereq): return False 
            
            visited[course] = 2
            result.append(course)
            return True 
        
        for i in range(numCourses):
            if not DFS(i): return []
        return result 
            
            

            