class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:

        res=[]
        def backtrack(col,leftRow,lowDiag,uppDiag,board):
            if col==n:
                res.append(["".join(row) for row in board])
                return
            for row in range(n):
                if leftRow[row]==0 and lowDiag[row+col]==0 and uppDiag[n-1+col-row]==0:
                    board[row][col]="Q"
                    leftRow[row]=1
                    lowDiag[row+col]=1
                    uppDiag[n-1+col-row]=1
                    backtrack(col+1,leftRow,lowDiag,uppDiag,board)
                    board[row][col]="."
                    leftRow[row]=0
                    lowDiag[row+col]=0
                    uppDiag[n-1+col-row]=0


        lowDiag=[0 for _ in range(2*n-1)]
        uppDiag=[0 for _ in range(2*n-1)]
        leftRow=[0 for _ in range(n)]
        board=[["."]*n for _ in range(n)]
        
        # print(board[0][1])
        backtrack(0,leftRow,lowDiag,uppDiag,board)
        return res
        
        # def backtrack(col,)