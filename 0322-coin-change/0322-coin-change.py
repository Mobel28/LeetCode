class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF=float('inf')
        dp=[[-1 for _ in range(amount+1)]for _ in range(len(coins)+1)]
        for i in range(len(coins)+1):
            for j in range(amount+1):
                if j==0:
                    dp[i][j]=0
                    continue
                if i==0:
                    dp[i][j]=INF
                    continue
                if coins[i-1]>j:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-coins[i-1]]+1)
        return dp[-1][-1] if dp[-1][-1]!=INF else -1