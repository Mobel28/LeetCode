class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n + 1)]
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        color=[-1]*(n+1)
        for node in range(1,n+1):
            if color[node]==-1:
                color[node]=0
            queue=deque([node])
            while queue:
                curr=queue.popleft()
                for i in graph[curr]:
                    if color[i]==-1:
                        color[i]=1-color[curr]
                        queue.append(i)
                    elif color[i]==color[curr]:
                        return False
        return True