"""
input: points list of int list 
output: k closest points to origin list of int list

Brute Force 
Scan the points and calculate all the distances from zero, store it to distance array
we can sort dist array in ascending order 
return kth 
Time complexity: O(NlogN)
Space complexity: O(N)

Min Heap 
while scanning the points 
    calculate dist
    we can push (dist, points)
    while heap size > k: 
        pop the heap so that heap maintains k closest points 

"""
import heapq 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def getDistance(x, y): 
            return math.sqrt(x**2 + y**2)
        
        heap = []
        for x, y in points: 
            dist = getDistance(x, y)
            heapq.heappush(heap, (-dist, [x, y]))

            while len(heap) > k: 
                heapq.heappop(heap)
            
        return [point for _, point in heap]

        