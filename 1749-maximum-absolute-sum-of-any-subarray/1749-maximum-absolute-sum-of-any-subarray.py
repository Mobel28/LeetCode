class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        def kadanae(nums):
            curr=0
            maxSum=float(-inf)
            for i in nums:
                curr+=i
                maxSum=max(maxSum,curr)
                if curr<0:
                    curr=0
            return maxSum
        return max(kadanae(nums),kadanae(x*-1 for x in nums ))