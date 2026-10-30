class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        piles = [1,3,100,2], h = 9
        k = 2

        H=1 [4,3,2]
        H=2 [2, 3, 2]
        H=3 [3, 2]
        H=4 [1, 2]
        H=5 [2]
        H=6 []

        1. Simulation 
            given k 
            h_count = 0 
            idx = 0
            while h_count < h: 
                hcount += piles[idx] // k
                idx += 1
        2. Range to search minimum k (1, max(piles))
           Binary search 
           l, r = 0, max(piles)
           if count(mid) --> search fh --> move r to mid 
           else --> search sh --> move l to mid 
        """
        def canFinishPiles(k): 
            h_count = 0 
            idx = 0 
            while idx < len(piles) : 
                h_count += piles[idx] // k
                if piles[idx] % k > 0:
                    h_count += 1
                if h_count > h: return False
                idx += 1 
            return True 
        
        # Binary search
        l, r = 1, max(piles)
        while l < r: 
            mid = (l + r)//2 
            if canFinishPiles(mid): 
                r = mid 
            else: 
                l = mid + 1 
        return l
        