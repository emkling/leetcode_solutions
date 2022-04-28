class MyQueue:

    def __init__(self):
        self.main_stack = []
        self.helper_stack = []

    def push(self, x: int) -> None:
        
        while self.main_stack:
            self.helper_stack.append(self.main_stack.pop())
            
        self.main_stack.append(x)
        
        while self.helper_stack:
            self.main_stack.append(self.helper_stack.pop())
        
    def pop(self) -> int:
        return self.main_stack.pop()
        

    def peek(self) -> int:
        if not self.main_stack:
            return 
        
        return self.main_stack[-1]

    def empty(self) -> bool:
        return True if len(self.main_stack) == 0 else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()