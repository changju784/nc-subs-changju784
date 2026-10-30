"""
input: points list of int list 
output: k closest points to origin list of int list

Brute Force 
Scan the points and calculate all the distances from zero, store it to distance array
we can sort dist array in ascending order 
return kth 


"""
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def getDistance(x, y): 
            return math.sqrt(x**2 + y**2)
        
        dists = {} 
        for x, y in points: 
            dist = getDistance(x, y)
            dists[(x, y)] = dist 
        
        sorted_dict = sorted(dists.items(), key=lambda x: x[1])
        
        result = []
        for i in range(k):
            point, _ = sorted_dict[i]
            result.append([point[0], point[1]])
            
        return result

        