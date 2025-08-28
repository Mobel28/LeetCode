class Solution:
    def clearDigits(self, s: str) -> str:
        res=[]
        for i in s:
            if i.isdigit():
                if res:
                    res.pop()
            else:
                res.append(i)
        return "".join(res)