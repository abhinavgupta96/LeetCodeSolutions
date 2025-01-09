class MinStack:

    def __init__(self):
        self.min = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min[-1] if self.min else val)
        self.min.append(val)
        return

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min.pop()
        return 

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return
        

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()