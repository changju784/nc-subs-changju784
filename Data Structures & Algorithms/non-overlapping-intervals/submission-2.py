class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        1. Sort by start 
        2. If overlapping longer gap should be removed 
        3. store non-overlapping 
        [[1,3],[2,4],[3,5],[1,6]] -> [[1,3],[1,6],[2,4],[3,5]]

        """
        intervals.sort(key = lambda x: x[0])
        l = 0
        minimum_removal = 0

        for r in range(1, len(intervals)): 
            if intervals[l][1] > intervals[r][0]: # overlaps 
                minimum_removal += 1 
                # determine l points 
                if intervals[l][1] > intervals[r][1]: 
                    l = r
            else: 
                l = r
        return minimum_removal



