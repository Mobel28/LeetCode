class Solution:
    def findMin(self, nums: list[int]) -> int:
        l,r=0,len(nums)-1 
        minVal=float(inf)
        while l<=r:
            m=(l+r)//2
            if nums[m]>=nums[l]:
                minVal=min(minVal,nums[l])
                l=m+1
            else:
                minVal=min(minVal,nums[r])
                r=m
        return minVal