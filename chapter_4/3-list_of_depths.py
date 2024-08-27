# Problem Description
# Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).

from ll_node import Node

def getLinkedListFromArray(array):
  nodes = [ Node(item) for item in array]
  for index in range(0, len(nodes)):
    if index < len(nodes) - 1:
      nodes[index].next = nodes[index + 1]
  return nodes[0]

def getLinkedListsByDepth(tree, root):
  linkedLists = []
  queue = [root]
  while len(queue) > 0:
    ll = getLinkedListFromArray(queue)
    linkedLists.append(ll)
    childsQueue = []
    for node in queue:
      if node in tree:
        childsQueue.extend(tree[node])
    queue = childsQueue
  return linkedLists

bst = {2: [1], 3: [2, 4], 7: [6], 8: [7, 9], 5: [3, 8], 12: [11], 13: [12, 14], 17: [16, 18], 15: [13, 17], 10: [5, 15]}
root = 10
linkedLists = getLinkedListsByDepth(bst, root)
for head in linkedLists:
  printList = []
  while head:
    printList.append(head.data)
    head = head.next
  print(printList)

# expected output:
# [10]
# [5, 15]
# [3, 8, 13, 17]
# [2, 4, 7, 9, 12, 14, 16, 18]
# [1, 6, 11]