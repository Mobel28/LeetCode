class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        profit=0
        for i in prices:
            cost=i-mini
            profit=max(cost,profit)
            mini=min(i,mini)
        return profit