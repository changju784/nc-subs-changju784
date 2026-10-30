class MinStack:

    def __init__(self):
        self.stack = [] # stores global elements 
        self.min_stack = [] # stores local minimum at that level

    def push(self, val: int) -> None:
        # whenever we push compare the current value with min stack push the smaller one. 
        self.stack.append(val)
        if self.min_stack: 
            smaller = min(self.min_stack[-1], val)
            self.min_stack.append(smaller)
        else: 
            self.min_stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop() 
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
