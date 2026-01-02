class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n=len(nums)//2
        dic={}
        for i in nums:
            dic[i]=dic.get(i,0)+1
            if dic[i]==n:
                return i
        return