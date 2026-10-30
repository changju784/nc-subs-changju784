class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [0] * n

        def climb(i): 
            if i == n:
                return 1
            if i > n: 
                return 0 
            if cache[i] > 0: 
                return cache[i]
            cache[i] = climb(i+1) + climb(i+2)
            return cache[i]

        climb(0)
        
        return max(cache)