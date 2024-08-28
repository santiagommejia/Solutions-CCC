# Description
# You are given a binary tree in which each node contains an integer value (which might be positive or negative). Design an algorithm to count the number of paths that sum to a given value. The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

from testing_functions import testFunction

class Node:

  def __init__(self, value, childs = None):
    self.value = value
    self.left = None
    self.right = None
    if childs:
      if len(childs) > 0:
        self.left = childs[0]
      if len(childs) > 1:
        self.right = childs[1]

def countPathsWithSum(root, targetSum, pathSum, pathSumsSet):
  if root is None:
    return 0
  pathSum += root.value
  diffValue = pathSum - targetSum
  count = 1 if pathSum == targetSum or diffValue in pathSumsSet else 0
  pathSumsSet.add(pathSum)
  leftCount = 0
  rightCount = 0
  if root.left:
    leftCount = countPathsWithSum(root.left, targetSum, pathSum, set(pathSumsSet))
  if root.right:
    rightCount = countPathsWithSum(root.right, targetSum, pathSum, set(pathSumsSet))
  return count + leftCount + rightCount

def testCountPathsWithSum(data):
  return countPathsWithSum(data[0], data[1], data[2], data[3])

# Tree definition 1
nodeG = Node(100)
nodeF = Node(5, [nodeG])
nodeE = Node(-2)
nodeD = Node(-1, [nodeF])
nodeC = Node(3, [nodeE])
nodeB = Node(2, [nodeD])
nodeA = Node(-1, [nodeB, nodeC])

# Tree definition 2
node3 = Node(3)
node2 = Node(2)
node4 = Node(4)
node11 = Node(11)
node5 = Node(5, [node3, node2])
nodem3 = Node(-3, [node4, node11])
node10 = Node(10, [node5, nodem3])

testCases = [[nodeA, 0, 0, set()], [nodeA, 4, 0, set()], [nodeA, 105, 0, set()], [nodeA, 1, 0, set()], [node10, 8, 0, set()]]
expectedResults = [2, 1, 1, 3, 2]
testFunction(testCases, expectedResults, testCountPathsWithSum)
