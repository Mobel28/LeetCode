from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color=[-1]*len(graph)
        for curr in range(len(graph)):
            if color[curr]==-1:
                color[curr]=0
                visit=set()
                queue=deque([curr])
                while queue:
                    curr = queue.popleft()
                    for neighbor in graph[curr]:
                        if color[neighbor] == -1:  
                            color[neighbor] = 1 - color[curr]  
                            queue.append(neighbor)
                        elif color[neighbor] == color[curr]: 
                            return False
        return True
