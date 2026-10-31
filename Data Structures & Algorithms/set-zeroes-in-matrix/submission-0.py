"""
rbr cbc inplace 
while rbr 
    once we found 0, 
    replace the entire row except 0 to -1 

while cbc
    once we found -1, 
    replcae it with 0 
    once we found 0, 
    replace the entire col by 0 


 1 2 3
 0 0 -1 
 6 7 8  

"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])
        found = False 

        # iterate through rbr, mark row with zero to -1 
        for r in range(row): 
            for c in range(col): 
                if matrix[r][c] == 0: 
                    found = True 
            if found: 
                for c in range(col): 
                    if matrix[r][c] != 0: 
                        matrix[r][c] = -1 
                found = False 
        
        found_zero_col = False 
        for c in range(col):
            # find zero and replace it with zero first 
            for r in range(row):
                if matrix[r][c] == 0: 
                    found_zero_col = True 
            if found_zero_col: 
                for r in range(row):
                    matrix[r][c] = 0 
                found_zero_col = False 

            # replace all -1 to 0 
            for r in range(row):
                if matrix[r][c] == -1: 
                    matrix[r][c] = 0 






        
        