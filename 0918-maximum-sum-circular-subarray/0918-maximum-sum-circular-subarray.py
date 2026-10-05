class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        globMax=nums[0]
        globMin=nums[0]
        currMax=float(-inf)
        currMin=float(inf)
        total=0
        for i in range(len(nums)):
            total+=nums[i]
            currMax=max(currMax+nums[i],nums[i])
            globMax=max(currMax,globMax)
            currMin=min(currMin+nums[i],nums[i])
            globMin=min(currMin,globMin)

        return max(globMax,total-globMin) if globMax>0 else globMax

