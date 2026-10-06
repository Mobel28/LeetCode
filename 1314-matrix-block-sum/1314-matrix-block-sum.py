class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        m=len(mat)
        n=len(mat[0])
        prefMat=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                prefMat[i+1][j+1]=mat[i][j]+prefMat[i+1][j]+prefMat[i][j+1]-prefMat[i][j]
        # print(prefMat)
        res=[[0]*n for _ in range(m)]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                r1=max(0,i-k)
                c1=max(0,j-k)
                r2=min(i+k,m-1)
                c2=min(j+k,n-1)
                res[i][j]=prefMat[r2+1][c2+1]-prefMat[r1][c2+1]-prefMat[r2+1][c1]+prefMat[r1][c1]
        return res