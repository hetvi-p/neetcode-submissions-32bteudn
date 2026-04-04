class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = []   
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minVal or self.minVal[-1] >= val:
            self.minVal.append(val)

    def pop(self) -> None:
        if self.top() == self.minVal[-1]:
            self.minVal.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minVal[-1]
        
