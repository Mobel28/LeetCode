class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        c=0
        for i in s:
            if i=='(':
                stack.append(i)
                print(stack)
            else:
                if stack:
                    stack.pop()
                else:
                    c+=1
        if not stack:
            return c
        else:
            return len(stack)+c