class MinStack:

    def __init__(self):
        self.stack=[]
        self.min=None

    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append(value)
            self.min=value
            return 
        if self.min>value:
            self.stack.append(2*value-self.min)
            self.min=value
        else:
            self.stack.append(value)
        return

    def pop(self) -> None:
        if self.min>self.stack[-1]:
            prevmin=2*self.min-self.stack[-1]
            self.min=prevmin
            self.stack.pop()
        else:
            self.stack.pop()    
    def top(self) -> int:
        if self.stack[-1]<self.min:
            return self.min
        else:
            return self.stack[-1]
    

    def getMin(self) -> int:
        return self.min
        
    #TC=O(1)
    #SC=O(1)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()