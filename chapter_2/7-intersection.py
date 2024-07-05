# Problem Description
# Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.

from support_functions import createLinkedListFromNodes, testFunction
from node import Node

def intersect(node1, node2):
    existingNodesSet = set()
    while node1:
        existingNodesSet.add(node1)
        node1 = node1.next
    while node2:
        if node2 in existingNodesSet:
            return True
        else:
            node2 = node2.next
    return False

def testIntersect(nodes):
    return intersect(nodes[0], nodes[1])

intersectNode = Node(3)
head1 = createLinkedListFromNodes([Node(1), Node(2), intersectNode, Node(4)])
head2 = createLinkedListFromNodes([Node(1), Node(2), Node(3), Node(4)])
head3 = createLinkedListFromNodes([Node(54), Node(12), intersectNode, Node(9)])
testCases = [[head1, head2], [head1, head3], [head2, head3]]
expectedResults = [False, True, False]
testFunction(testCases, expectedResults, testIntersect)