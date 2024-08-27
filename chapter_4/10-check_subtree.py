# Problem Description
# T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an algorithm to determine if T2 is a subtree of T1.
# A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2. That is, if you cut off the tree at node n, the two trees would be identical.

from graph_tree import Node, bst_root, node2, node4, node6, node10, node11
from testing_functions import testFunction

def preOrder(node):
  if not node:
    return 'x'
  if not node.childs:
    return str(node.data) + '|x|x'
  if len(node.childs) == 1:
    return str(node.data) + '|' + preOrder(node.childs[0])
  if len(node.childs) == 2:
    return str(node.data) + '|' + preOrder(node.childs[0]) + '|' + preOrder(node.childs[1])

def calculateT1NodePreOrders(node, isSubTree, preOrderT2):
  nodePreOrder = str(node.data)
  if isSubTree:
    return nodePreOrder, True
  elif not node:
    return 'x', isSubTree
  elif not node.childs:
    nodePreOrder = str(node.data) + '|x|x'
    return nodePreOrder, (isSubTree or nodePreOrder == preOrderT2)
  elif len(node.childs) == 1:
    leftPreOrder, leftIsSubTree = calculateT1NodePreOrders(node.childs[0], isSubTree, preOrderT2)
    nodePreOrder = str(node.data) + '|' + leftPreOrder
    return nodePreOrder, (isSubTree or leftIsSubTree or nodePreOrder == preOrderT2)
  else:
    leftPreOrder, leftIsSubTree = calculateT1NodePreOrders(node.childs[0], isSubTree, preOrderT2)
    rightPreOrder, rightIsSubTree = calculateT1NodePreOrders(node.childs[1], isSubTree, preOrderT2)
    nodePreOrder = str(node.data) + '|' + leftPreOrder + '|' + rightPreOrder
    return nodePreOrder, (isSubTree or leftIsSubTree or rightIsSubTree or nodePreOrder == preOrderT2)

def testIsSubTreeFunction(nodes):
  rootT1 = nodes[0]
  rootT2 = nodes[1] 
  preOrderT2 = preOrder(rootT2)
  _, isSubTree = calculateT1NodePreOrders(rootT1, False, preOrderT2)
  return isSubTree
  
dummyNode = Node(100)
testCases = [[bst_root, node2], [bst_root, node4], [bst_root, node6], [bst_root, node10], [bst_root, node11], [bst_root, dummyNode]]
expectedResults = [True, True, True, True, True, False]
testFunction(testCases, expectedResults, testIsSubTreeFunction)
