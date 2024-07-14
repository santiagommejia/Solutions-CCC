# Problem Description
# An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type). They cannot select which specific animal they would like. Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use the built-in LinkedList data structure.

class AnimalNode:

  def __init__(self, type, name, age):
    self.type = type
    self.name = name
    self.age = age
    self.next = None

  def print(self):
    print('Animal:', self.type, self.name, self.age)

class AnimalQueue:

  def __init__(self):
    self.head = None

  def enqueue(self, animalNode):
    if self.head == None:
      self.head = animalNode
    else:
      n = self.head
      while n.next != None:
        n = n.next
      n.next = animalNode

  def dequeueAny(self):
    if self.head == None:
      print('queue is empty')
      return
    else:
      head = self.head
      self.head = self.head.next
      return head
    
  def dequeueDog(self):
    return self.dequeueType('dog')
  
  def dequeueCat(self):
    return self.dequeueType('cat')
      
  def dequeueType(self, type):
    if self.head == None:
      print('queue is empty')
      return
    else: 
      n = self.head
      if n.type == type:
        self.head = self.head.next
        return n
      while n.next != None and n.next.type != type:
        n = n.next
      # next is None or animal
      if n.next == None:
        print(f'No {type}s in queue')
        return
      else:
        animal = n.next
        n.next = n.next.next
        return animal

dog1 = AnimalNode('dog', 'Firulais', 1)
cat1 = AnimalNode('cat', 'Figaro', 1)
dog2 = AnimalNode('dog', 'Pedro', 2)
cat2 = AnimalNode('cat', 'Anastasio', 2)
dog3 = AnimalNode('dog', 'Coco', 3)
cat3 = AnimalNode('cat', 'Milly', 3)

queue = AnimalQueue()
queue.enqueue(dog1)
queue.enqueue(cat1)
queue.enqueue(dog2)
queue.enqueue(cat2)
queue.enqueue(dog3)
queue.enqueue(cat3)

# deque
anyAnimal = queue.dequeueAny()
if anyAnimal:
  anyAnimal.print()

# dequeDog
firstDog = queue.dequeueDog()
secondDog = queue.dequeueDog()
if (firstDog and secondDog):
  firstDog.print()
  secondDog.print()

# dequeCat
firstCat = queue.dequeueCat()
secondCat = queue.dequeueCat()
if (firstCat and secondCat):
  firstCat.print()
  secondCat.print()



