# Problem Description
# Implement an algorithm to find the kth to last element of a singly linked list.

from node import Node
from support_functions import createLinkedListFromArray, printLinkedList

def kthToLast(head, k):
    if k < 0:
        print('K must be a postive number')
        return None
    if not head or not head.data:
        return head
    elementPositionDict = {}
    counter = 0
    node = head
    while node:
        counter += 1
        elementPositionDict[counter] = node
        node = node.next
    if counter - k < 1:
        print('K must be less than the number of nodes')
        return None 
    else:
        return elementPositionDict[counter - k]


baseArray = [1,2,3,4,5,6,7,8,9,10,11,12]
k = 4
head = createLinkedListFromArray(baseArray)
kthToLastNode = kthToLast(head, k)
if kthToLastNode:
    print(kthToLastNode.data)
