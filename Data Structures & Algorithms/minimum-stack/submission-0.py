class MinStack:

    def __init__(self):
        self.stack = [] # initialize the stack
        self.minStack = [] # initialize a stack where we'll keep track of the minimum
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        # determine what the minimum is by comparing our previous minimum to last minimum we calculated
            # this is the top of minStack 
        val = min(val, self.minStack[-1] if self.minStack else val) # if the minStack is empty, the value is automatically the minimum
        self.minStack.append(val) # append that minimum value to the min stack

    def pop(self) -> None:
        # pop from both the stack and minstack to keep the stacks aligned
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1] # top is equivalent to peek
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
