class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        d={}
        for v,e in dislikes:
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
        color=[-1]*n
        for nodes in d:
            if color[nodes-1]==-1:
                color[nodes-1]=0
                queue=deque([nodes])
            while queue:
                curr=queue.popleft()
                for i in d[curr]:
                    if color[i-1]==-1:
                        color[i-1]=1-color[curr-1]
                        queue.append(i)
                    elif color[i-1]==color[curr-1]:
                        return False
        return True