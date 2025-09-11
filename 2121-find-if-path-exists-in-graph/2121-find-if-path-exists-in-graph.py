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
        def bfs(dict,sou,des):
            visit=set()
            queue=[sou]
            visit.add(sou)
            while queue:
                node=queue.pop(0)
                for i in dict[node]:
                    if i not in visit:
                        visit.add(i)
                        queue.append(i)
            if des in visit:
                return True
            else:
                return False
        return bfs(d,source,destination)
