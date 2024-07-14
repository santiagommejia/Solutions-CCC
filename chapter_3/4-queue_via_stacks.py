# Problem Description
# Implement a MyQueue class which implements a queue using two stacks.

class MyQueue:

    def __init__(self):
        self.firstStack = []
        self.secondStack = []
    
    def add(self, item):
        self.firstStack.append(item)
    
    def remove(self):
        if len(self.secondStack) > 0:
            return self.secondStack.pop()
        elif len(self.firstStack) > 0:
            self.__clearFirstStack()
            return self.remove()
        else:
            print('MyQueue is empty')
            return None
    
    def peek(self):
        firstStackLen = len(self.firstStack)
        secondStackLen = len(self.secondStack)
        if secondStackLen == 0 and firstStackLen == 0:
            print('MyQueue is empty')
            return None
        else:
            if len(self.secondStack) > 0:
                return self.secondStack[secondStackLen - 1]
            else:
                self.__clearFirstStack()
                return self.peek()
    
    def isEmpty(self):
        return len(self.firstStack) == 0 and len(self.secondStack) == 0
    
    def __clearFirstStack(self):
        if len(self.firstStack) > 0:
            while len(self.firstStack):
                self.secondStack.append(self.firstStack.pop())
        return

queue = MyQueue()
for i in range(8):
    queue.add(i)
for i in range(4):
    print(queue.peek())
    queue.remove()
for i in range(10,15):
    queue.add(i)
print(queue.peek())
for i in range(7):
    queue.remove()
print(queue.peek())
print(queue.isEmpty())
for i in range(3):
    queue.remove()
print(queue.isEmpty())