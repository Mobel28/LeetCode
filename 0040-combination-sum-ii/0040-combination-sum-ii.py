class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        hashMap={}
        candidates.sort()
        def rec(output,j,ssum):
            if ssum>target:
                return
            if ssum==target:
                ans.append(output.copy())
                    
            for i in range(j,len(candidates)):
                if i>j and candidates[i]==candidates[i-1]:
                    continue
                output.append(candidates[i])
                rec(output,i+1,ssum+candidates[i])
                output.pop()
        rec([],0,0)
        return ans
            