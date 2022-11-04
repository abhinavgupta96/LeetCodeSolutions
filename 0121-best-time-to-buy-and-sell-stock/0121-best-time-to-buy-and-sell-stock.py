class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ##2 approaches implemented
        
        ##approach1 - from leetcode
        max_prof = 0
        min_price = prices[0]
        for i in range(len(prices)):
            if prices[i] < min_price: ##compare every value with min value, i.e time to buy
                min_price = prices[i]
            elif prices[i] - min_price > max_prof: ##if not min_value, compute profit, if greater than current max profit
                max_prof = prices[i] - min_price
        return max_prof
    ##approach2 - from neetcode
    # l,r = 0,1 ##left is where we buy, right is where we sell
    # max_prof = 0
    # while r < len(prices):
    #     if prices[l] < prices[r]: #if price to buy is lower than sell
    #         prof = prices[r] - prices[l]
    #         max_prof = max(prof,max_prof) #checks if current profit is bigger than current max profit
    #     else:
    #         l = r #if buy price is higher than sell, then move current buy price to sell price
    #     r+=1 ##increment r in either case
    # return max_prof