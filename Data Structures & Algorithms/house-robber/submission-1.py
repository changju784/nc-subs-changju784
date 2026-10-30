class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Dynamic Programming + Recursion 

        Initiate len(nums) of array of 1s. 
        Recursively record amount of money stole starting from each house
        Whenever reaches the end (n-1, n-2) return the amount of money 
        If we have already have stolen by checking cache, just return the money  

        """
        n = len(nums)
        cache = [-1] * n

        def DFS(i): 
            if i == n - 1: # when reached end
                return nums[i]
            if i >= n: 
                return 0 
            if cache[i] > -1:
                return cache[i]
            rob_curr = nums[i] + DFS(i+2)
            skip_curr = DFS(i+1)
            cache[i] = max(rob_curr, skip_curr)
            return cache[i]
        return DFS(0)
        

            