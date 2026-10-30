"""
input: list of integers, could be negative, duplicates 
output: kth largest element in the list.

1. sorting O(nlogn) O(1)
sort this by descending order 
get the kth index 

2. min heap O(Nlogk) O(N)
while iterating through the nums 
store the element in heap size of k 
after iteration, root element of heap will be kth largest element 
[2,3,1,5,4] k = 2

[5,4]

"""
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # iterate through the nums 
        heap = [] 
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k: 
                heapq.heappop(heap)
        return heap[0]
        