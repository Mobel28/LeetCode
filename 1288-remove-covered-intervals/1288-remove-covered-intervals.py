class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0],-x[1]))
        res=0
        maxLimit=0
        for i,j in intervals:
            if j>maxLimit:
                res+=1
                maxLimit=j
        return res