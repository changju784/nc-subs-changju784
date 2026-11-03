"""
input: 2d integer grid that has ascending order sorted by rows, target int 
output: boolean if target exists in the grid or not 

Brute Force 
Scan the entire 2d matrix 
    rbr, cbc, top-left to bottom-right 
    check if target exists 
TC: O(M*N)
SC: O(1)

Coalesing + Binary Search 
Imagine if this entire 2d grid is coalesced in 1d memory space 
Inplace binary search
** The first integer of every row is greater than the last interger of previous row 
target = 11
1 
10 11 12 13 
14 

Two Binary Search 
Row binary search (To get row index where our target can be located)
    Search from first column 

"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        def find_row():
            l, r = 0, row - 1
            while l <= r:
                mid = (l + r) // 2
                if matrix[mid][0] <= target <= matrix[mid][-1]:
                    return mid
                elif target < matrix[mid][0]:
                    r = mid -1 
                else:
                    l = mid + 1
            return -1
        
        def find_in_row(row_idx):
            l, r = 0, col - 1
            while l <= r:
                mid = (l + r) // 2
                if matrix[row_idx][mid] == target:
                    return True 
                elif target < matrix[row_idx][mid]:
                    r = mid - 1 
                else:
                    l = mid + 1
            return False 

        # binary search on first column 
        row_idx = find_row()
        if row_idx == -1: 
            return False 

        # binary search on target row 
        if find_in_row(row_idx): 
            return True 
        return False 
            

        