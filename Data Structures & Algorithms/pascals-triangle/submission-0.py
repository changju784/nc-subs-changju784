"""
Initialize rows 
Current row[j] = previous row[j-1] + [j+1], where 0 < j < len(current row)
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1] * n for n in range(1, numRows+1)]
        if len(triangle) < 3: 
            return triangle
        for i in range(2, len(triangle)):
            curr = triangle[i]
            prev = triangle[i-1]
            for j in range(1, len(curr)-1):
                triangle[i][j] = prev[j-1] + prev[j]
        return triangle
        