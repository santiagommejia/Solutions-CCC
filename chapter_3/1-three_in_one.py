# Problem Description
# Describe how you could use a single array to implement three stacks.

class Stack3in1:

    def __init__(self):
        self.stacksArray = []
        self.stacks = [{'start': 0, 'length': 0} for _ in range(3)]

    def pop(self, stack):
        if stack < 0 or stack > 2:
            print('stack is out of range, only stacks 0, 1 and 2 are supported')
            return
        elementToPop = None
        if self.stacks[stack]['length'] == 0:
            print('stack is empty')
            return
        if stack == 0:
            elementToPop = self.stacksArray[self.stacks[0]['length'] - 1]
            del self.stacksArray[self.stacks[0]['length'] - 1]
            self.stacks[0]['length'] -= 1
            self.stacks[1]['start'] = max(0, self.stacks[1]['start'] - 1)
            self.stacks[2]['start'] = max(0, self.stacks[2]['start'] - 1)
        elif stack == 1:
            elementToPop = self.stacksArray[self.stacks[0]['start'] + self.stacks[0]['length'] + self.stacks[1]['length'] - 1]
            del self.stacksArray[self.stacks[0]['start'] + self.stacks[0]['length'] + self.stacks[1]['length'] - 1]
            self.stacks[1]['length'] -= 1
            self.stacks[2]['start'] = max(0, self.stacks[2]['start'] - 1)
        elif stack == 2:
            elementToPop = self.stacksArray[self.stacks[1]['start'] + self.stacks[1]['length'] + self.stacks[2]['length'] - 1]
            del self.stacksArray[self.stacks[1]['start'] + self.stacks[1]['length'] + self.stacks[2]['length'] - 1]
            self.stacks[2]['length'] -= 1
        return elementToPop

    def push(self, stack, item):
        if stack < 0 or stack > 2:
            print('stack is out of range, only stacks 0, 1 and 2 are supported')
            return
        pos = self.stacks[stack]['start'] + self.stacks[stack]['length']
        self.stacksArray.insert(pos, item)
        for i in range(stack, 3):
            if i == stack:
                self.stacks[i]['length'] += 1
            else:
                self.stacks[i]['start'] +=1
        return

    def peek(self, stack):
        if stack < 0 or stack > 2:
            print('stack is out of range, only stacks 0, 1 and 2 are supported')
            return
        pos = self.stacks[stack]['start'] + self.stacks[stack]['length'] - 1
        return self.stacksArray[pos]

    def isEmpty(self, stack):
        if stack < 0 or stack > 2:
            print('stack is out of range, only stacks 0, 1 and 2 are supported')
            return
        return self.stacks[stack]['length'] == 0

# fill stacks
stacks = Stack3in1()
print(stacks.isEmpty(0))
stacks.push(0, 6)
print(stacks.isEmpty(0))
stacks.push(0, 7)
stacks.push(1, 9)
stacks.push(1, 0)
stacks.push(2, 1)
stacks.push(2, 2)
print(stacks.peek(0))
print(stacks.peek(1))
print(stacks.peek(2))
stacks.push(1,5)
print(stacks.peek(1))
stacks.pop(1)
print(stacks.peek(1))
stacks.push(2,8)
print(stacks.peek(2))
print(stacks.isEmpty(2))
stacks.pop(2)
stacks.pop(2)
stacks.pop(2)
print(stacks.isEmpty(2))