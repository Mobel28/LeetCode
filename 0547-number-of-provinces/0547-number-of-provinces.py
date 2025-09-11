from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        d={}
        for i in range(1,len(isConnected)+1):
            d[i]=[]
            for j in range(len(isConnected)):
                if isConnected[i-1][j]!=0 and i!=j+1:
                    d[i].append(j+1)
        visit=set()
        provinces=0
        def bfs(source):
            queue=deque([source])
            while queue:
                node=queue.popleft()
                for i in d[node]:
                    if i not in visit:
                        visit.add(i)
                        queue.append(i)
        for v in d:
            if v not in visit:
                visit.add(v)
                provinces+=1
                bfs(v)
        return provinces 

        
        

