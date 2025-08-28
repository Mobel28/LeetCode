class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in{'(','{','['}:
                stack.append(i)
            else:
                if stack:
                    v=stack.pop()
                    if (v=='(' and i==')') or (v=='{' and i=='}') or (v=='['and i==']'):
                        continue
                    else:
                        return False
                else:
                    return False
        return not stack
