# Problem Description
# A binary search tree was created by traversing through an array from left to right and inserting each element. Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.

# EXAMPLE
# Input:
#     2
#    / \
#   1   3
# Output: {2, 1, 3}, {2, 3, 1}

from graph_tree import Node

def getArrayFromBST(node):
  if not node:
    return []
  if not node.childs:
    return [[node.data]]
  leftChild = node.childs[0] if len(node.childs) > 0 else None
  rightChild = node.childs[1] if len(node.childs) > 1 else None
  leftArrays = getArrayFromBST(leftChild) if leftChild else []
  rightArrays = getArrayFromBST(rightChild) if rightChild else []
  results = []
  for leftArray in leftArrays:
    for rightArray in rightArrays:
      inOrderResult = [node.data] + leftArray + rightArray
      postOrderResult = [node.data] + rightArray + leftArray
      results.append(inOrderResult)
      results.append(postOrderResult)
  return results

print('Case 1:')
node1 = Node(1)
node3 = Node(3)
root = Node(2, [node1, node3])
results = getArrayFromBST(root)
for result in results:
  print(result)

print('Case 2:')
node5 = Node(5)
node7 = Node(7)
node2 = Node(2, [node1, node3])
node6 = Node(6, [node5, node7])
node4 = Node(4, [node2, node6])
results = getArrayFromBST(node4)
for result in results:
  print(result)