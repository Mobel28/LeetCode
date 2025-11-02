class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid=[[0]*n for _ in range(m)]
        for i,j in guards:
            grid[i][j]=1
        for i,j in walls:
            grid[i][j]=2
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        def guard_pos(gr,gc,dr,dc):
            nr,nc=gr+dr,gc+dc
            while 0<=nr<m and 0<=nc<n:
                if grid[nr][nc]==1 or grid[nr][nc]==2:
                    break
                if grid[nr][nc]==0:
                    grid[nr][nc]=3
                nr+=dr
                nc+=dc
        for gr,gc in guards:
            for dr,dc in directions:
                guard_pos(gr,gc,dr,dc)
        count=0
        for r in range(m):
            for c in range(n):
                if grid[r][c]==0:
                    count+=1
        return count
