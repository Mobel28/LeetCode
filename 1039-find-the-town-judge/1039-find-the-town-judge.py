class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        outdegree=[0]*n
        indegree=[0]*n
        for e,v in trust:
            outdegree[e-1]+=1
            indegree[v-1]+=1
        print(outdegree)
        print(indegree)
        for i in range(n):
            if outdegree[i]==0 and indegree[i]==n-1:
                return i+1
        return -1