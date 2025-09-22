class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d={}
        count=0
        val=0
        for i in nums:
            d[i]=d.get(i,0)+1
            if d[i]>count:
                count=d[i]
        for i in d.values():
            if i==count:
                val+=i

        return val