"""
Input: flowers interval, people visiting at time people[i]
output: number of bloomed flowers that people can see at people[i]

Brute Force 
For each people 
    initailize count = 0
    For each flower interval
        Check if people[i] overlaps
            If so count up 
    store count to result[i]
N = len(people), M = len(flowers)
TC: O(N*M) -> what if N or M is super large?
SC: O(1)

Key point: 
1. flowers people can see = # started flower before i - # ended flower before i 
2. divide start/end of flower interval and sort them, 
3. Find where i can be located for each and subtract start - end 

Binary Search 
Sort start and end ascending order 
For each people 
    Binary search on start 
    Binary search on end 
    result[i] = start - end 
TC: O(MlogM + NlogM)
SC: O(M)
"""
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        sorted_start = sorted([f[0] for f in flowers])
        sorted_end = sorted([f[1] for f in flowers])        
        result = [0] * len(people)
     
        for i in range(len(people)): 
            # binary search on start 
            sl, sr = 0, len(sorted_start)
            while sl < sr: 
                mid = (sl + sr)//2
                if sorted_start[mid] <= people[i]: 
                    sl = mid + 1
                else: 
                    sr = mid 

            # binary search on end 
            el, er = 0, len(sorted_end)
            while el < er: 
                mid = (el + er) // 2
                if sorted_end[mid] < people[i]: 
                    el = mid + 1
                else:
                    er = mid 

            result[i] = sl - el

        return result
            

            

