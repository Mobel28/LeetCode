class Solution(object):
    def twoSum(self, nums, target):
        dic={}
        for i in range(len(nums)):
            req=target-nums[i]
            if req in dic:
                return dic[req],i
            else:
                dic[nums[i]]=i
        # TC=O(NlogN)
        # SC=O(1)