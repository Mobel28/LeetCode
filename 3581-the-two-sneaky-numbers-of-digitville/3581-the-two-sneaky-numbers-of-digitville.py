class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        res=[]
        for key,val in d.items():
            if val>1:
                res.append(key)
        return res