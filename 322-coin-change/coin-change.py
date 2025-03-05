class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        maxAmount = float('inf')

        dp = [0] + [maxAmount] * amount

        for coin in coins:
            for currentAmount in range(coin, amount+1) : 
                dp[currentAmount] = min(dp[currentAmount], dp[currentAmount - coin]+1)
        
        return -1 if dp[amount] == maxAmount else dp[amount] 