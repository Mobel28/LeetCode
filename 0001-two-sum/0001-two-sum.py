class Solution(object):
    def twoSum(self, nums, target):
        rem={}
        for i in range(len(nums)):
            num=target-nums[i]
            # print(num,rem)
            if num in rem:
                return [rem[num],i]
            
            rem[nums[i]]=i
        
        