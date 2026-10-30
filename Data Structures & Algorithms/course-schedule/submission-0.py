from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        goal is to take all the courses from 0 to numCourses-1 
        prerequisite is a condition, order doesn't matter. 
        Determine if there's cycle within the graph. 

        ex) numCourses = 4 prereq = [[0,1], [1, 2], [2,3], [3,1]]
        3 -> 2 -> 1 -> 0
        """
        hash_map = defaultdict(list) 

        for k, v in prerequisites: 
            hash_map[k].append(v)
        
        # 0 - not visited, 1 - visiting, 2 - visited
        visited = [0] * numCourses

        def DFS(course):
            if visited[course] == 1: # cycle detected
                return False 
            if visited[course] == 2: 
                return True
            
            visited[course] = 1 

            for prereq in hash_map[course]: 
                if not DFS(prereq): return False 
            
            visited[course] = 2
            return True

        for i in range(numCourses): 
            if not DFS(i): return False
        return True

