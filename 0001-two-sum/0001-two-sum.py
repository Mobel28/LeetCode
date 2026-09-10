class Solution(object):
    def twoSum(self, nums, target):
        rem={}
        for i in range(len(nums)):
            if nums[i] in rem:
                return rem[nums[i]],i 
            req=target-nums[i]
            rem[req]=i
                   