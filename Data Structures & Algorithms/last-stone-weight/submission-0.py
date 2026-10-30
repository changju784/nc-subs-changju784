"""
input: integer list -> simulate elimination by removing two heaviest stone. 
output: return the last remaining stone's weight

constraints: 
0 < len(stones)
0 < stone[i]
nums could be duplicates 

    [2,3,6,2,4]
    [1,0,0,0,0]
i=0  6, 4  
i=1  3, 2
i=2  2, 2

Max Heap 
while len(heap) > 1
every round we want to pop the heap twice 
in the first pop we will get the max 
pop the second biggest element
    compare the values 
    if they are same 
    if first is bigger, than push first - second back to heap
element left in the heap will be the answer 
if len is zero return 0
[]  
TC: O(N + NlogN)
SC: O(N)
"""
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # convert list to heap
        max_heap =  [-1 * stone for stone in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1: 
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)
            if first > second: 
                heapq.heappush(max_heap, -(first - second))
        if len(max_heap) > 0: 
            return -max_heap[0]
        return 0

        