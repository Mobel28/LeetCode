class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        check=nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            check=max(nums[i],check+nums[i])
            res=max(check,res)
        return res