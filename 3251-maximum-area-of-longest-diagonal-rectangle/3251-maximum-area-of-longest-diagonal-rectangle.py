class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        diagonal=float('-inf')
        area=0
        for i in dimensions:
            temp=(i[0]*i[0])+i[1]*i[1]
            temp=temp**0.5
            if temp>diagonal or (temp==diagonal and i[0]*i[1]>area):
                diagonal=temp
                area=i[0]*i[1]
                # print(area)
        return area
