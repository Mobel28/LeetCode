class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count=0
        temp=0
        for r in nums:
            if r==1:
                temp+=1
            else:
                count=max(temp,count)
                temp=0
        count=max(count,temp)
        return count