class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1 for _ in range(n)]
        def solve(i):
            if i==1 or i==0:
                return 1
            if dp[i-1]!=-1:
                return dp[i-1]
            
            dp[i-1]=solve(i-1)+solve(i-2)
            return dp[i-1]
        return solve(n)