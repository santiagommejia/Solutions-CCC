# Problem Description
# Write a program to sort a stack such that the smallest items are on the top. You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.

import random

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        if len(self.stack) > 1:
            return self.stack[len(self.stack) - 1]
        else:
            print('Stack is empty')
            return None

    def isEmpty(self):
        return len(self.stack) == 0
    
    def print(self):
        print(self.stack)

    def order(self):
        auxStack = []
        while len(self.stack) > 0:
            topElement = self.stack.pop()
            if len(self.stack) > 0:
                peekElement = self.stack[len(self.stack) - 1]
                if topElement <= peekElement:
                    auxStack.append(topElement)
                else:
                    auxStack.append(peekElement)
                    self.stack.pop()
                    self.stack.append(topElement)
            else:
                auxStack.append(topElement)
                isOrdered = True
                while len(auxStack) > 0:
                    auxTopElement = auxStack.pop()
                    if len(auxStack) > 0:
                        newAuxTopElement = auxStack[len(auxStack) - 1]
                        if auxTopElement < newAuxTopElement:
                            isOrdered = False
                    self.stack.append(auxTopElement)
                if isOrdered:
                    break
        return
    
stack = Stack()
for _ in range(10):
    stack.push(random.randint(0,15))
stack.print()
stack.order()
stack.print()



