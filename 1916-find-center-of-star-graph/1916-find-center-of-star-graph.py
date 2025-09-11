class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        star=[0]*(len(edges)+1)
        for e,v in edges:
            star[e-1]+=1
            star[v-1]+=1
        print(star)
        for i in range(len(star)):
            if star[i]==len(edges):
                return i+1
        