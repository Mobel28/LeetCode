from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n  
        for node in range(n):
            if color[node] == -1: 
                color[node] = 0
                queue = deque([node])
                while queue:
                    curr = queue.popleft()
                    for neighbor in graph[curr]:
                        if color[neighbor] == -1:  
                            color[neighbor] = 1 - color[curr]  
                            queue.append(neighbor)
                        elif color[neighbor] == color[curr]: 
                            return False
        return True
