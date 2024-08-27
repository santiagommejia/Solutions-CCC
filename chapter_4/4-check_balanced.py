# Problem Description
# Implement a function to check if a binary tree is balanced. For the purposes of this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.

from testing_functions import testFunction

def getHeightsTree(tree, node, heightTree = None):
  # print('init', tree, node, heightTree)
  if heightTree is None:
    heightTree = {}
  if node not in tree:
    return heightTree, 0, True
  else:
    nodes = tree[node]
    maxDepth = 0
    isBalanced = True
    if len(nodes) >= 1:
      heightTree, leftDepth, leftIsBalanced = getHeightsTree(tree, nodes[0], heightTree)
      # print('left side', heightTree, leftDepth)
      heightTree[nodes[0]] = leftDepth
      maxDepth = leftDepth
      isBalanced = leftIsBalanced
    if len(nodes) == 2:
      heightTree, rightDepth, rightIsBalanced = getHeightsTree(tree, nodes[1], heightTree)
      # print('right side', heightTree, rightDepth)
      heightTree[nodes[1]] = rightDepth
      maxDepth = max(leftDepth, rightDepth)
      isBalanced = False if not leftIsBalanced or not rightIsBalanced else abs(rightDepth - leftDepth) <= 1
    # print('returning', heightTree, maxDepth + 1)
    return heightTree, maxDepth + 1, isBalanced

def isBalancedTree(tree, root):
  heightTree, rootDepth, isBalanced = getHeightsTree(tree, root)
  heightTree[root] = rootDepth
  return isBalanced

def testIsBalancedTree(params):
  bst = params[0]
  root = params[1]
  return isBalancedTree(bst, root)


bst1 = {2: [1], 3: [2, 4], 7: [6], 8: [7, 9], 5: [3, 8], 12: [11], 13: [12, 14], 17: [16, 18], 15: [13, 17], 10: [5, 15]}
bst2 = {0: [-1], 1: [0], 2: [1, 3], 4: [2, 6], 6: [5, 7]}
bst3 = {1: [0], 2: [1, 3], 4: [2, 6], 6: [5, 7]}
bst4 = {2: [1], 3: [2, 4], 7: [6], 8: [7, 9], 5: [3, 8], 11: [10.5], 12: [11], 13: [12, 14], 17: [16, 18], 15: [13, 17], 10: [5, 15]}
root1 = 10
root2 = 4
root3 = 4
root4 = 10

testCases = [[bst1, root1], [bst2, root2], [bst3, root3], [bst4, root4]]
expectedResults = [True, False, True, False]
testFunction(testCases, expectedResults, testIsBalancedTree)