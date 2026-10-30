from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums: 
            freq[num] += 1 
        
        heap = [] 
        for key, val in freq.items(): 
            heapq.heappush(heap, (val, key))
            if len(heap) > k: 
                heapq.heappop(heap)
        return [key for val, key in heap]
        
        