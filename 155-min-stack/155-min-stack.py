class MinStack:

    def __init__(self):
        self.s1 = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.s1.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        
    def pop(self) -> None:
        self.s1.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.s1[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()