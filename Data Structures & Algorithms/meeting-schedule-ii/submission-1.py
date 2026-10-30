"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


"""
Min heap O(NlogN) O(N)
1. we can sort the intervals by start 
2. we can store earliest end time in min heap 
3. if current start time is greater or equal than heap's end 
    we can pop the heap 
4. length of min heap becomes number of meeting rooms we need. 

Two Pointers 
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # intervals.sort(key=lambda x: x.start)
        # min_heap = [] 
        # for interval in intervals: 
        #     if min_heap and min_heap[0] <= interval.start:
        #         heapq.heappop(min_heap)
        #     heapq.heappush(min_heap, interval.end)
        # return len(min_heap)
        start = sorted([x.start for x in intervals])
        end = sorted([x.end for x in intervals]) 
        res = count = 0
        s, e = 0, 0 

        while s < len(intervals):
            if start[s] < end[e]: # new meeting starts before earliest one ends 
                s += 1
                count += 1 
            else: 
                e += 1
                count -= 1
            res = max(res, count)
        return res
             
