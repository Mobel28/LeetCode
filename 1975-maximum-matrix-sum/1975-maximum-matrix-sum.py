class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        max_sum=0
        neg_count=0
        min_abs=float('inf')
        for row in matrix:
            for val in row:
                max_sum+=abs(val)
                if val<0:
                    neg_count+=1
                if abs(val)<min_abs:
                    min_abs=abs(val)
        if neg_count%2==0:
            return max_sum
        else:
            return (max_sum-(min_abs)*2)