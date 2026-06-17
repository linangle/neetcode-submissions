class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
    # optimal dp    
        # dp[a] represents the number of ways to form amount a
        dp = [0] * (amount + 1) 
        dp[0] = 1 # base case : one way to form amount 0
        for i in range(len(coins) - 1, -1, -1): # iterate in reverse order
            # for each coin, iterate through all amounts from 1 to amount
            for a in range(1, amount + 1):
            # if the current coin value is less than or equal to the amount
                # add d[a - coin] to dp[a]
                dp[a] += dp[a - coins[i]] if coins[i] <= a else 0
        return dp[amount]