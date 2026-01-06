class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        row=[""]*numRows
        curr_row=0
        direction=1
        for ch in s:
            row[curr_row]+=ch
            if curr_row==numRows-1:
                direction=-1
            elif curr_row==0:
                direction=1
            curr_row+=direction
        return "".join(row)