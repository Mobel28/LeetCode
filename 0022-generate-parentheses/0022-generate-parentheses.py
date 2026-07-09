class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def paranthesis(popen,pclose,temp):
            if len(temp)==n*2:
                res.append(temp)
                temp=""
                return
            if popen<n:
                paranthesis(popen+1,pclose,temp+'(')
            if pclose<popen:
                paranthesis(popen,pclose+1,temp+')')

        paranthesis(0,0,"")
        return res
