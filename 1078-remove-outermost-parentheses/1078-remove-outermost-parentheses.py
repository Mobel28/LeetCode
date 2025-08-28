class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=[]
        b=0
        for i in s:
            if i=='(':
                if b>0:
                    res.append(i)
                b+=1
            else:
                b-=1
                if b>0:
                    res.append(i)
        return "".join(res)

