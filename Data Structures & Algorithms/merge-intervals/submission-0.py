class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        [[2,4],[1,3],[4,5]]
        [[1,5], [2,4], [4,5]]
        result = [[]]
        1. Sort the intervals by start 
        2. stack - last interval, 
            peek last interval end with curr start 
            mergeable - pop stack and merge intervals and push
            not - don't pop push curr
        T: O(NlogN) S: O(N)
        """
        stack = []
        intervals.sort(key=lambda x: x[0])

        for i in range(len(intervals)): 
            if not stack: 
                stack.append(intervals[i])
            else: 
                if stack[-1][1] >= intervals[i][0]: 
                    last_start, last_end = stack.pop()
                    stack.append([last_start, max(last_end, intervals[i][1])])
                else: 
                    stack.append(intervals[i])
        return stack
