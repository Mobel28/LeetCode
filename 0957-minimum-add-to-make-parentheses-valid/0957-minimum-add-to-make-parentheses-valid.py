class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        c=0
        for i in s:
            if i=='(':
                stack.append(i)
                print(stack)
            else:
                if stack and stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(i)
        return len(stack)+c