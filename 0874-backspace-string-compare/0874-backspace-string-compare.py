class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def stack(st):
            res=[]
            for i in st:
                if i=="#":
                    if res:
                        res.pop()
                else:
                    res.append(i)
            return res
        return stack(s)==stack(t)
