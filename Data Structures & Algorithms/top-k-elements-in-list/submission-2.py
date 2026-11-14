"""
input: integer nums, int k 
output: return the k most frequent elements 

ex) [1, 2,2, 3,3,3] k = 2
[2, 3] 

Hashmap 
Build frequency table key - num, value - freq 
1) Sort the table by value asc/dec return the slice -> O(MlogM) where M is # of unique nums 
2) Min heap size of k
Iterate through freq table, store (freq, num) in min heap
pop the heap when size reaches k so that in the heap we only maintain k most freq elements. -> O(Mlogk) O(M*K)
"""
from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build a freq table 
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        # iterate through freq table and maintain minheap size of k 
        min_heap = []
        for num, freq in freq.items(): 
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k: 
                heapq.heappop(min_heap)
        result = []
        while min_heap: 
            _, num = heapq.heappop(min_heap)
            result.append(num)
        return result 
