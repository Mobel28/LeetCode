class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        listidx={ch:i for i,ch in enumerate(s)}
        stack=[]
        inset=set()
        for i,ch in enumerate(s):
            if ch in stack:
                continue
            while stack and ch < stack[-1] and i < listidx[stack[-1]]:
                inset.remove(stack.pop())
            stack.append(ch)
            inset.add(ch)
        
        return "".join(stack)