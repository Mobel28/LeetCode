class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        has={}
        for i in nums:
            has[i]=has.get(i,0)+1
        for key,val in has.items():
            if val>len(nums)/2:
                return key
        return -1
        #TC=O(N)