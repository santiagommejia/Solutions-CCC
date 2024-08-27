# Problem Description
# Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search tree. You may assume that each node has a link to its parent.

from graph_tree import Node, bst_root, node1, node2, node3, node4, node5, node6, node8, node9, node10, node11, node12
from testing_functions import testFunction

def maxNode(node1, node2):
  if node1 is None:
    return node2
  return node1 if node1.data >= node2.data else node2

def findNextNode(node, prevNode):
  childs = node.childs
  parent = node.parent
  node.marked = True
  if childs is None or len(childs) == 1:
    if parent is None:
      return node
    else:
      return maxNode(findNextNode(parent, node), node) if parent.data < node.data else parent
  elif len(childs) == 2:
    if parent is None:
      return childs[1] if node == prevNode else node
    else:
      if node.data > prevNode.data:
        return node
      else:
        return childs[1] if not childs[1].marked else findNextNode(parent, prevNode)
        

def testFindNextNode(node):
  nextNode = findNextNode(node, node)
  return None if nextNode == node else nextNode.data

testCases = [node1, node2, node3, node4, node5, node6, bst_root, node8, node9, node10, node11, node12]
expectedResults = [2, 3, 4, 6, 6, 7, 10, 9, 10, 12, 12, None]
testFunction(testCases, expectedResults, testFindNextNode)