class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        1. Sort by start 
        2. If overlapping with larger end -> remove 
        3. use two pointers l, r l keeps the most recent non-overlapping interval. 
        4. when overlaps compare two interval ends and move l to r 
        5. if no overlap move l to r 

        Improve: 
        1. Sort by end 
        """
        intervals.sort(key = lambda x: x[1])
        l = 0
        minimum_removal = 0

        for r in range(1, len(intervals)): 
            if intervals[l][1] > intervals[r][0]: # overlaps 
                minimum_removal += 1 
            else: 
                l = r
        return minimum_removal



