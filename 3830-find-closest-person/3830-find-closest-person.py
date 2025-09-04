class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        difx=abs(z-x)
        dify=abs(z-y)
        if difx<dify:
            return 1
        elif dify<difx:
            return 2
        else:
            return 0