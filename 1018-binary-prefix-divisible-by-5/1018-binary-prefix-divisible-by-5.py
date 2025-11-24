class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res=[]
        val=0
        for i in nums:
            val=(val*2+i)%5
            res.append(val==0)
        return res