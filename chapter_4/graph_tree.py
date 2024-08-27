class Node:

  def __init__(self, data, childs = None):
    self.data = data
    self.parent = None
    self.childs = childs
    self.marked = False

  def addParent(self, parent):
    self.parent = parent

  def addChild(self, child):
    if self.childs is None:
      self.childs = []
    self.childs.append(child)

  def printChilds(self):
    for child in self.childs:
      print(child.data)


node1 = Node(1)
node3 = Node(3)
node5 = Node(5)
node8 = Node(8)
node11 = Node(11)
node2 = Node(2, [node1, node3])
node6 = Node(6, [node5])
node9 = Node(9, [node8])
node12 = Node(12, [node11])
node4 = Node(4, [node2, node6])
node10 = Node(10, [node9, node12])
bst_root = Node(7, [node4, node10])
node4.addParent(bst_root)
node10.addParent(bst_root)
node2.addParent(node4)
node6.addParent(node4)
node9.addParent(node10)
node12.addParent(node10)
node1.addParent(node2)
node3.addParent(node2)
node5.addParent(node6)
node8.addParent(node9)
node11.addParent(node12)