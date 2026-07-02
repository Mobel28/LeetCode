class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m,n=len(grid),len(grid[0])
        start=health-grid[0][0]
        if start<=0:
            return False
        best=[[-1]*n for _ in range(m)]
        best[0][0]=start
        max_heap=[(-start,0,0)]
        dirs=[(0,1),(0,-1),(1,0),(-1,0)]
        while max_heap:
            h,x,y=heappop(max_heap)
            h=-h
            if (x,y)==(m-1,n-1):
                return True
            if h<best[x][y]:
                continue
            for dx,dy in dirs:
                nx=dx+x
                ny=dy+y
                if 0<=nx<m and 0<=ny<n:
                    nh=h-grid[nx][ny]
                    if nh>0 and nh>best[nx][ny]:
                        best[nx][ny]=nh
                        heappush(max_heap,(-nh,nx,ny))
        return False