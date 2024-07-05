# Problem Description
# Write code to remove duplicates from an unsorted linked list.
# How would you solve this problem if a temporary buffer is not allowed?

from support_functions import createLinkedListFromArray, printLinkedList

def removeDuplicates(head):
    if not head or not head.next or not head.data:
        return head
    existingValuesSet = set([head.data])
    node = head
    while node and node.next:
        next = node.next
        if not next.data in existingValuesSet:
            existingValuesSet.add(next.data)
            node = next
        else:
            node.next = next.next
    return head

def removeDuplicatesNoBuffer(head):
    if not head or not head.next or not head.data:
        return head
    h = head
    node = head
    while node:
        if node and node.next:
            if head.data == node.next.data:
                node.next = node.next.next
            else:
                node = node.next
        else:
            head = head.next
            node = head
    return h    

baseList = [1,2,3,5,2,7,8,1,1,5,9]
head = createLinkedListFromArray(baseList)
headNoBuffer = createLinkedListFromArray(baseList)
printLinkedList(head, 'before:')
printLinkedList(removeDuplicates(head), 'after:')
printLinkedList(removeDuplicatesNoBuffer(headNoBuffer), 'after:')