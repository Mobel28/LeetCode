class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        suffmin=[-1]*len(nums)
        suffmin[-1]=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            suffmin[i]=min(nums[i],suffmin[i+1])
        prefmax=float('-inf')
        for i in range(len(nums)):
            prefmax=max(nums[i],prefmax)
            if prefmax-suffmin[i]<=k:
                return i
        return -1