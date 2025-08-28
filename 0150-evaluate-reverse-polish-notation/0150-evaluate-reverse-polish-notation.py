class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i[-1].isdigit():
                stack.append(int(i))
            else:
                if len(stack)>=2:
                    a=stack.pop()
                    b=stack.pop()
                if i=='+':
                    stack.append(a+b)
                elif i=='-':
                    stack.append(b-a)
                elif i=='*':
                    stack.append(a*b)
                elif i=='/':
                    stack.append(int(b/a))
        return stack.pop()