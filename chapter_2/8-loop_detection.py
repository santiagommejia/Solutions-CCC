# Problem Description
# Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.
# Definition
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list.
# Example
# Input: A -> B -> C -> D -> E -> C [the same C as earlier]
# Output: C

from support_functions import createLinkedListFromArray, testFunction
from node import Node

def loopDetection(node):
    existingNodesSet = set()
    while node:
        if node in existingNodesSet:
            return True
        else:
            existingNodesSet.add(node)
        node = node.next
    return False

loopedNode = Node(5)
loopedNode.append_node_to_tail(Node(6))
loopedNode.append_node_to_tail(loopedNode)
node = createLinkedListFromArray([1,2,3,4])
node.append_node_to_tail(loopedNode)
testCases = [node, loopedNode, createLinkedListFromArray([1,2,3,4,5,4,3,2,1])]
expectedResults = [True, True, False]
testFunction(testCases, expectedResults, loopDetection)
