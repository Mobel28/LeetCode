class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0
        
        for row in matrix:
            # Build histogram heights
            for c in range(cols):
                if row[c] == "1":
                    heights[c] += 1
                else:
                    heights[c] = 0
            
            # Compute largest rectangle in histogram
            max_area = max(max_area, self.largestRectangleArea(heights))
        
        return max_area
    
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        heights.append(0)  # Sentinel to flush stack
        
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        
        heights.pop()
        return max_area