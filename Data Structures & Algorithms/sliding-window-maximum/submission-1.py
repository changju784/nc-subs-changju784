"""
input: integer list num, integer k 
output: integer list, collect maximums while window size of k reaching the end 
constraints: 
1 <= k <= len(nums)
num could be neg or zero 

[1,2,1,0,4,2,6] k = 3
 L
     R
[2, 2, 4, 4, 6]

Brute force 
scan the nums with window
    copy the subarray 
    record max 
TC: O(N*k)
SC: O(k)

Max Heap 
- need to determine when we pop the max out from heap 
- we need to keep track of indices b.c. from indices we can tell if max is out of window
- need to clarify order of operation (push, pop, record)

build max heap by iterating through 0 to k-1 (initial window)
    while building heap push tuple (-num, index)
iterate from k to n-1: 
    push nums[r] to heap 
    increment left pointer 
    check if root of max heap index with left pointer 
        if it's out of window -> pop 
    push max_heap[0] to result

TC: O(Nlogk)
SC: O(N)
"""
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # build initial heap from 0 to k-1
        max_heap = []
        for i in range(k):
            heapq.heappush(max_heap, (-nums[i], i))
        
        # two pointers window size of k
        l = 0
        result = [-max_heap[0][0]]
        for r in range(k, len(nums)):
            heapq.heappush(max_heap, (-nums[r], r)) 
            l += 1
            while max_heap[0][1] < l: # pop root when out of window boundary 
                heapq.heappop(max_heap)
            result.append(-max_heap[0][0])
            print(nums[l])
        return result

        