class Solution(object):
    def twoSum(self, nums, target):
      dict={}
      for i in range(len(nums)):
        num=nums[i]
        rem=target-num
        if rem in dict:
            return [dict[rem],i]
        dict[num]=i
        