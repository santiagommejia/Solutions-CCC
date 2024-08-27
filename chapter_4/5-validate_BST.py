# Problem Description
# Implement a function to check if a binary tree is a binary search tree.

from testing_functions import testFunction

def isBST(tree, root):
  if root not in tree:
    return True
  length = len(tree[root])
  if length < 1 or length > 2:
    return False
  if length <= 2:
    left = tree[root][0]
    if left > root:
      return False
  if length == 2:
    right = tree[root][1]
    if root >= right:
      return False
  return isBST(tree, tree[root][0]) if length == 1 else isBST(tree, tree[root][0]) and isBST(tree, tree[root][1])

def testIsBST(params):
  bst = params[0]
  root = params[1]
  return isBST(bst, root)

bst1 = {2: [1], 3: [2, 4], 7: [6], 8: [7, 9], 5: [3, 8], 12: [11], 13: [12, 14], 17: [16, 18], 15: [13, 17], 10: [5, 15]}
bst2 = {0: [-1], 1: [0], 2: [1, 3], 4: [2, 6], 6: [5, 7]}
bst3 = {1: [0], 2: [1, 3], 4: [2, 6], 6: [5, 7]}
bst4 = {2: [1], 3: [2, 4], 7: [6], 8: [7, 9], 5: [3, 8], 12: [11], 13: [58, 14], 17: [16, 18], 15: [13, 17], 10: [5, 15]}
root1 = 10
root2 = 4
root3 = 4
root4 = 10
testCases = [[bst1, root1],[bst2, root2],[bst3, root3],[bst4, root4]]
expectedResults = [True, True, True, False]
testFunction(testCases, expectedResults, testIsBST)