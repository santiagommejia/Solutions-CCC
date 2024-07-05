# Problem Description
# You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
# Example
# Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.
# Follow Up
# Suppose the digits are stored in forward order. Repeat the above problem.
# Example
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295.
# Output: 9 -> 1 -> 2. That is, 912.

from support_functions import createLinkedListFromArray, printLinkedList
from node import Node

def getNum(node):
    number = 0
    while node:
        number = number*10 + node.data
        node = node.next
    return number

def getReverseNum(node):
    if node.next == None:
        return node.data
    return getReverseNum(node.next) * 10 + node.data

def sumListsReverse(node1, node2):
    num = getReverseNum(node1) + getReverseNum(node2)
    head = None
    while num > 1:
        digit = int(num % 10)
        if head is None:
            head = Node(digit)
        else:
            head.append_node_to_tail(Node(digit))
        num = int(num/10)
    return head

def sumLists(node1, node2):
    num = getNum(node1) + getNum(node2)
    numStr = str(num)
    head = None
    for char in numStr:
        digit = int(char)
        if head is None:
            head = Node(digit)
        else:
            head.append_node_to_tail(Node(digit))
    return head
    
node1 = createLinkedListFromArray([7,1,6])
node2 = createLinkedListFromArray([5,9,2])
node3 = createLinkedListFromArray([6,1,7])
node4 = createLinkedListFromArray([2,9,5])
printLinkedList(sumListsReverse(node1, node2))
printLinkedList(sumLists(node3, node4))