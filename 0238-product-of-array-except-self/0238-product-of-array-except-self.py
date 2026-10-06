class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res=[1 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i-1>=0:
                res[i]=nums[i-1]*res[i-1]
        rp=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            res[i]=res[i]*rp
            rp*=nums[i]
        return res
