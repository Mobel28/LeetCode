class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        res=1
        longest=1
        tmin=nums[0]

        for i in nums:
            if i==tmin:
                continue
            
            if tmin==i-1:
                longest+=1
            
            else:
                res=max(longest,res)
                longest=1
            tmin=i
        return max(res,longest)

    #TC=O(nlogn)
    #SC=O(1)