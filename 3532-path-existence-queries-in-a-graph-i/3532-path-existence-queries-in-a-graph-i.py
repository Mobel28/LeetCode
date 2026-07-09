class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        comp=[-1]*n
        comp[0]=0
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]<=maxDiff:
                comp[i]=comp[i-1]
            else:
                comp[i]=comp[i-1]+1
        res=[]
        for l,r in queries:
            if comp[l]==comp[r]:
                res.append(True)
            else:
                res.append(False)
        return res