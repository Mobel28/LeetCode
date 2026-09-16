class Solution:
    def totalNQueens(self, n: int) -> int:
        res=0
        def backtrack(col,leftRow,lowDiag,uppDiag):
            nonlocal res
            if col==n:
                res+=1
                return
            for row in range(n):
                if leftRow[row]==0 and lowDiag[row+col]==0 and uppDiag[(n-1)+(col-row)]==0:
                    leftRow[row]=1
                    lowDiag[row+col]=1
                    uppDiag[(n-1)+(col-row)]=1
                    backtrack(col+1,leftRow,lowDiag,uppDiag)
                    leftRow[row]=0
                    lowDiag[row+col]=0
                    uppDiag[(n-1)+(col-row)]=0
        leftRow=[0]*n
        lowDiag=[0 for _ in range(2*n-1)]
        uppDiag=[0 for _ in range(2*n-1)]
        backtrack(0,leftRow,lowDiag,uppDiag)
        return res
