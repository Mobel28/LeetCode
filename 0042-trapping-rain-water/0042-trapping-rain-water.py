class Solution:
    def trap(self, height: list[int]) -> int:
        rightMax=[-1 for _ in range(len(height))]
        rightMax[-1]=height[-1]
        j=len(height)-2
        while j>=0:
            rightMax[j]=max(rightMax[j+1],height[j])
            j-=1
        total=0
        leftMax=float('-inf')
        for i in range(len(height)):
            leftMax=max(leftMax,height[i])
            total+=min(leftMax,rightMax[i])-height[i]
        return total