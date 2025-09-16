class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans=['']*len(score)
        temp=sorted(enumerate(score),key=lambda x:-x[1])
        for rank,(idx,val) in enumerate(temp):
            if rank==0:
                ans[idx]="Gold Medal"
            elif rank==1:
                ans[idx]="Silver Medal"
            elif rank==2:
                ans[idx]="Bronze Medal"
            else:
                ans[idx]=str(rank+1)
        return ans
