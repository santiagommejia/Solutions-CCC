# Problem Description
# Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure. Note: This is not necessarily a binary search tree.

from graph_tree import bst_root, node1, node2, node4, node5, node6, node8, node9, node10, node11, node12
from testing_functions import testFunction

def findFirstCommonAncestor(root, p, q):
  if not root or root == p or root == q:
    return root
  if root.childs is None or root.childs is []:
    return None
  leftNode = root.childs[0] if len(root.childs) > 0 else None
  rightNode = root.childs[1] if len(root.childs) > 1 else None
  left = findFirstCommonAncestor(leftNode, p, q)
  right = findFirstCommonAncestor(rightNode, p, q)
  if left and right:
    return root
  elif left:
    return left
  elif right:
    return right
  else:
    return None

def testFindFirstCommonAncestor(nodes):
  root = nodes[0]
  p = nodes[1]
  q = nodes[2]
  return findFirstCommonAncestor(root, p, q)

root = bst_root

testCases = [[root, node2, node5], [root, node4, node10], [root, node2, node11], [root, node1, node2], [root, node5, node6], [root, node9, node12], [root, node8, node11]]
expectedResults = [node4, root, root, node2, node6, node10, node10]

testFunction(testCases, expectedResults, testFindFirstCommonAncestor)