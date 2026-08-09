class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        temp=sorted(nums)
        res=1
        longest=1
        tmin=temp[0]

        for i in temp:
            if i==tmin:
                continue
            
            if tmin==i-1:
                longest+=1
            
            else:
                res=max(longest,res)
                longest=1
            tmin=i
        return max(res,longest)

