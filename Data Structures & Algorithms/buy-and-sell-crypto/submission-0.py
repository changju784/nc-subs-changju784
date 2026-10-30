class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # descending order --> no transaction 
        '''
        [10,8,7,5,2]
            ^          
        min_price = 8
        max_profit = 0
        '''
        min_price = float('inf')
        max_profit = 0 

        for curr_price in prices: 
            min_price = min(min_price, curr_price)
            max_profit = max(max_profit, curr_price - min_price)

        return max_profit 