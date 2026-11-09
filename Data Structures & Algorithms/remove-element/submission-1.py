"""
Two pass O(n) O(1)
Iterate through nums and Count how many val exist in nums 
Set right pointer to len(nums)-count 
While iterating through nums left pointer - 0 to n - val - 1
    When we find val from left pointer, 
    swap with right 
    proceed right 

[2, 2, 3, 3]
          R
    L
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for num in nums:
            if num == val:
                count += 1

        k = len(nums) - count       
        r = k                       
        for l in range(k):
            if nums[l] == val:
                while nums[r] == val:          # ← 추가: 뒤쪽에서 val이 아닌 원소 찾기
                    r += 1
                nums[l], nums[r] = nums[r], nums[l]
                r += 1
        return k



        