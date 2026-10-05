class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr=0
        maxSum=float(-inf)
        for i in nums:
            curr+=i
            maxSum=max(maxSum,curr)
            if curr<0:
                curr=0
        return maxSum