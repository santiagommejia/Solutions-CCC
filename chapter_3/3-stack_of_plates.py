# Problem Description
# Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack (that is, pop() should return the same values as it would if there were just a single stack).
# Follow up
# Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.

class SetOfStacks:

    def __init__(self, threshold):
        self.threshold = threshold
        self.stacks = [[]]

    def push(self, item):
        currentStackIndex = len(self.stacks) - 1
        currentStack = self.stacks[currentStackIndex]
        if len(currentStack) >= self.threshold:
            self.stacks.append([item])
        else:
            self.stacks[currentStackIndex].append(item)
        return
    
    def pop(self):
        currentStackIndex = len(self.stacks) - 1
        currentStack = self.stacks[currentStackIndex]
        if len(currentStack) == 0 and currentStackIndex == 0:
            print('Stack is empty')
            return None
        else:
            elementToPop = currentStack.pop() 
            if len(currentStack) == 0 and currentStackIndex > 0:
                del self.stacks[currentStackIndex]
            return elementToPop

    def popAt(self, stackIndex):
        if stackIndex < 0 or stackIndex > len(self.stacks) - 1:
            print('Stack index is out of range')
            return None
        stack = self.stacks[stackIndex]
        if len(stack) == 0 and stackIndex == 0:
            print('Stack is empty')
            return None
        elif len(stack) == 0 and stackIndex > 0:
            print('Stack is empty, removing stack')
            del self.stacks[stackIndex]
            return None
        else:
            elementToPop = stack.pop() 
            if len(stack) == 0 and stackIndex > 0:
                del self.stacks[stackIndex]
            return elementToPop
        
    def printStack(self):
        print(self.stacks)

stack = SetOfStacks(3)
for i in range(1,10):
    stack.push(i)
for _ in range(2):
    stack.pop()
    stack.printStack()
for _ in range(3):
    stack.popAt(1)
    stack.printStack()
stack.popAt(1)
stack.printStack()


