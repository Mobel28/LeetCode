class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total=0
        for i in range(1,len(points)):
            x1,y1=points[i-1]
            x2,y2=points[i]
            dx=abs(x1-x2)
            dy=abs(y1-y2)
            total+=max(dx,dy)
        return total