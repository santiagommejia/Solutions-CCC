# Problem Description
# Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements less than x. The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.
# Example
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

from node import Node
from support_functions import createLinkedListFromArray, printLinkedList

def partition(head, partition):
    leftHead = None
    rightHead = None
    while head:
        next = head.next
        head.next = None
        if head.data < partition:
            if leftHead is None:
                leftHead = head
            else: 
                leftHead.append_node_to_tail(head)
        else: 
            if rightHead is None:
                rightHead = head
            else:
                rightHead.append_node_to_tail(head)
        head = next
    if leftHead is None:
        return rightHead
    else:
        leftHead.append_node_to_tail(rightHead)
        return leftHead


baseList = [7,2,3,5,2,7,8,1,1,5,9]
partitionNumber = 5
head = createLinkedListFromArray(baseList)
printLinkedList(head, 'before: ')
printLinkedList(partition(head, partitionNumber), 'after: ')



