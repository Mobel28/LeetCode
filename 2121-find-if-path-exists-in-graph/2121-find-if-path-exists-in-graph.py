class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n==1:
            return True
        d={}
        for v,e in edges:
            if v in d:
                d[v].append(e)
            else:
                d[v]=[]
                d[v].append(e)
            if e in d:
                d[e].append(v)
            else:
                d[e]=[]
                d[e].append(v)
        visit=set()
        def bfs(source,dict,dest):
            queue=[source]
            visit.add(source)
            while queue:
                node=queue.pop(0)
                for i in d[node]:
                    if i not in visit:
                        visit.add(i)
                        queue.append(i)
            return dest in visit   
        return bfs(source,d,destination)        