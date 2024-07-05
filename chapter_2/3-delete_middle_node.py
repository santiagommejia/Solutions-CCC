# Problem Description
# Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.
# Example
# Input: the node c from the linked list a -> b -> c -> d -> e -> f
# Result: nothing is returned, but the new linked list looks like a -> b -> d -> e -> f

from support_functions import createLinkedListFromArray, printLinkedList

def removeMiddleNode(head, nodeData):
    if not head or not head.data or not nodeData:
        return head
    node = head
    while node.next:
        if node.next.data == nodeData:
            node.next = node.next.next
            return head
        else:
            node = node.next
    print('Node not found')
    return head

baseArray = ['a','b','c','d','e','f']
head = createLinkedListFromArray(baseArray)
printLinkedList(head, 'before: ')
head = removeMiddleNode(head, 'c')
printLinkedList(head, 'after: ')

    