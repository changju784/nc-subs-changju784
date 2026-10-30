class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        (i,j) -> (j, (n-1)-i)
        outer ring -> inner ring, step k replacement 4 cycles. 
        k = 0 to (n // 2)
        layer k range -> (k, k) to (k, n-k-2)
        """
        n = len(matrix)
        row = 0
        for row in range(n//2): # outer ring to inner ring
            for col in range(row, (n-1)-row): 
                """
                p0 = (row, col)
                p1 = (col, n-1-row)
                p2 = (n-1-row, n-1-col)
                p3 = (n-1-col, row)
                """
                temp = matrix[row][col] # store curr
                matrix[row][col] = matrix[n-1-col][row] # p0 <- p3
                matrix[n-1-col][row] = matrix[n-1-row][n-1-col] # p3 <- p2
                matrix[n-1-row][n-1-col] = matrix[col][n-1-row] # p2 <- p1
                matrix[col][n-1-row] = temp # p1 <- p0
        return None