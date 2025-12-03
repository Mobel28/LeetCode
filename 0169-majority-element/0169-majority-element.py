class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Moore Voting 
        elem=0
        count=0
        for i in nums:
            if count==0:
                elem=i
                count+=1
            elif i==elem:
                count+=1
            else:
                count-=1
        return elem
        #SC=O(1)
        #TC=O(N)