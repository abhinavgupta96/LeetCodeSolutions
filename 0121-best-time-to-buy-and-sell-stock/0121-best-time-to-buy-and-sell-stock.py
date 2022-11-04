class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ##2 approaches implemented
        
        ##approach1 - from leetcode
        max_prof = 0
        min_price = prices[0]
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_prof:
                max_prof = prices[i] - min_price
        return max_prof