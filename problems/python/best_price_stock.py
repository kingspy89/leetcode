class Solution(object):
    def maxProfit(self, prices):
        min_n=float('inf')
        max_n=0
        for price in prices:
           
            if price < min_n:
                min_n = price
            elif price - min_n > max_n: 
                max_n = price - min_n
        
        return max_n
