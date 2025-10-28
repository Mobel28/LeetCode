class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic={}
        for i in nums:
            dic[i]=dic.get(i,0)+1
        for val,key in dic.items():
            if key==1:
                return val
        return