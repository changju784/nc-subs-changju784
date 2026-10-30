class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Array is sorted 
        Binary search with two pointers 

        if sum l r are > target --> move r to l 
        if sum l r are < target --> move l to r 
        if sum l r == target  return 
        """
        l, r = 0, len(numbers)-1
        while l < r: 
            if numbers[l] + numbers[r] > target: # move r
                r -= 1
            elif numbers[l] + numbers[r] < target: # move l
                l += 1
            else: 
                return [l+1, r+1]
        
