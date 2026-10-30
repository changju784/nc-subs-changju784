import heapq
class MedianFinder:

    def __init__(self):
        self.first_half = []  # put smaller numbers in neg -> pop largest in smaller group
        self.second_half = [] # put larger numbers -> pop smallest in larger group 
        
    def addNum(self, num: int) -> None:
        # push negated incoming num to first half 
        heapq.heappush(self.first_half, -num)
        heapq.heappush(self.second_half, -heapq.heappop(self.first_half))

        if len(self.first_half) < len(self.second_half): # balance 
            heapq.heappush(self.first_half, -1 * heapq.heappop(self.second_half))

    def findMedian(self) -> float:
        if (len(self.first_half) + len(self.second_half)) % 2: # odd
            return -1 * self.first_half[0] 
        else: 
            return (-1 * self.first_half[0] + self.second_half[0])/2
        
        