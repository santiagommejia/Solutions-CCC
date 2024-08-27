# Problem Description
# You are implementing a binary tree class from scratch which, in addition to insert, find, and delete, has a method getRandomNode() which returns a random node from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm for getRandomNode, and explain how you would implement the rest of the methods.

import random

class Node:

  def __init__(self, value, childs = None):
    self.value = value
    self.left = childs[0] if (childs and len(childs) > 0) else None
    self.right = childs[1] if (childs and len(childs) > 1) else None

class BinaryTree:

  def __init__(self, root):
    self.root = root
    self.height = 1

  def calculateTreeHeight(self, root, isRoot):
    if root is None:
      return 0
    leftHeight = self.calculateTreeHeight(root.left, False)
    rightHeight = self.calculateTreeHeight(root.right, False)
    height = max(leftHeight, rightHeight) + 1
    if isRoot:
      self.height = height
    return height
  
  def insert(self, node):
    n = self.root
    isInserted = False
    while not isInserted:
      if node.value < n.value:
        if n.left:
          n = n.left
        else:
          n.left = node
          isInserted = True
      elif node.value > n.value:
        if n.right:
          n = n.right
        else:
          n.right = node
          isInserted = True
      else:
        print('Node value already in tree.')
        break
    height = self.calculateTreeHeight(self.root, True)
    self.height = height

  def find(self, value):
    n = self.root
    while n:
      if n.value == value:
        return n
      else:
        n = n.left if value < n.value else n.right
    return None
  
  def delete(self, root, value):
    if root is None:
      return root
    if value < root.value:
      root.left = self.delete(root.left, value)
    elif value > root.value:
      root.right = self.delete(root.right, value)
    else:
      if root.left is None:
        return root.right
      elif root.right is None:
        return root.left
      successor = self.findMin(root.right)
      root.value = successor.value
      root.right = self.delete(root.right, successor.value)
    return root
  
  def findMin(self, node):
    if node.left is None:
      return node
    return self.findMin(node.left)
  
  def print(self):
    queue = [self.root]
    while queue:
      node = queue[0]
      print(f"parent {node.value} has left child {node.left.value if node.left else 'None'} and right child {node.right.value if node.right else 'None'}.")
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)
      queue.pop(0)
  
  def getRandomNode(self):
    random_level = random.randint(0, self.height * 2)
    node = self.root
    while random_level > 0:
      random_level -= 1
      if node.left and node.right:
        random_direction = random.randint(0, 1)
        node = node.left if random_direction == 0 else node.right
      elif node.left:
        node = node.left
      if not node:
        node = self.root
    return node

# With direct child definition  
# node1 = Node(1)
# node3 = Node(3)
# node5 = Node(5)
# node8 = Node(8)
# node11 = Node(11)
# node2 = Node(2, [node1, node3])
# node6 = Node(6, [node5])
# node9 = Node(9, [node8])
# node12 = Node(12, [node11])
# node4 = Node(4, [node2, node6])
# node10 = Node(10, [node9, node12])
# bst_root = Node(7, [node4, node10])
# tree = BinaryTree(bst_root)
# tree.calculateTreeHeight(bst_root, True)
# # tree.print()

# With child insertion
node1 = Node(1)
node3 = Node(3)
node5 = Node(5)
node8 = Node(8)
node11 = Node(11)
node2 = Node(2)
node6 = Node(6)
node9 = Node(9)
node12 = Node(12)
node4 = Node(4)
node10 = Node(10)
bst_root = Node(7)
tree = BinaryTree(bst_root)
tree.insert(node4)
tree.insert(node10)
tree.insert(node2)
tree.insert(node6)
tree.insert(node9)
tree.insert(node12)
tree.insert(node1)
tree.insert(node3)
tree.insert(node5)
tree.insert(node8)
tree.insert(node11)
tree.calculateTreeHeight(bst_root, True)
# tree.print()

print('Random values')
for i in range(10):
  randomNode = tree.getRandomNode()
  print('Random node result: ', randomNode.value)

print()
print('Find values')
for i in range(15):
  findNode = tree.find(i)
  print(f"{'Found value: ' + str(findNode.value) if findNode else 'Value ' + str(i) + ' not found' }")

print('Delete Node 10')
tree.delete(bst_root, 10)
tree.print()