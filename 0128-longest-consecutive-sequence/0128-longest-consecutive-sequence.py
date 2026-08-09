class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums :
            return 0
        tempSet=set(nums)
        longest=1
        curr=1
        for i in tempSet:
            if i-1 in tempSet:
                continue
            else:
                while i+curr in tempSet:
                    curr+=1
                    
                longest=max(curr,longest)
                curr=1
        return longest

    #TC=O(N)
    #SC=O(N)