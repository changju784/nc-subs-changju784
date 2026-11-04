"""
1 2 2 1 
 3 1 2
1  3  2

Hashmap 
Iterate through each row 
    For each row record where brick edge exists 
    key - index, value - count of edge exists in that index 
minimal number of crossed brick 
number of rows - edge exists in that bridge,
"""
from collections import defaultdict
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_map = defaultdict(int)
        for row in wall: 
            curr_sum = 0 
            for i in range(len(row)-1): 
                curr_sum += row[i] 
                edge_map[curr_sum] += 1
        if len(edge_map) == 0:
            return len(wall)
        return len(wall) - max(edge_map.values()) 
        