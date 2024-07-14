# Problem Description
# How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop and min should all operate in O(1) time.

class MinStack:
    
    def __init__(self):
        self.stack = []
        self.minStack = []
    
    def push(self, item):
        self.stack.append(item)
        if len(self.minStack) == 0 or item < self.minStack[len(self.minStack) - 1]:
            self.minStack.append(item)
        
    def pop(self):
        stackLen = len(self.stack)
        if stackLen > 0:
            minStackLen = len(self.minStack)
            minElementToPop = self.stack[stackLen - 1]
            if minStackLen >= 1 and minElementToPop == self.minStack[minStackLen - 1]:
                del self.minStack[minStackLen - 1]
            return self.stack.pop()
        else:
            return None
    
    def min(self):
        minStackLen = len(self.minStack)
        stackLen = len(self.stack)
        if minStackLen is 0 and stackLen is 0:
            print('Stack is empty')
            return None
        return self.minStack[minStackLen - 1] if minStackLen > 1 else self.stack[stackLen - 1] 
    
stack = MinStack()
stack.push(5)
print(stack.min())
stack.push(7)
print(stack.min())
stack.push(3)
print(stack.min())
stack.push(1)
print(stack.min())
stack.push(8)
print(stack.min())
print()

# 5 7 3 1 8
stack.pop()
print(stack.min())
stack.pop()
print(stack.min())
stack.pop()
print(stack.min())
stack.pop()
print(stack.min())
stack.pop()
print(stack.min())
stack.pop()
print(stack.min())