class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[1 for _ in range(m)]
        for i in range(1,n):
            for j in range(1,m):
                dp[j]=dp[j-1]+dp[j]
        print(dp)
        return dp[m-1]