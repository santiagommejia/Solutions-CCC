# Problem Description
# Implement a function to check if a linked list is a palindrome.

from support_functions import createLinkedListFromArray, testFunction

def isPalindrome(node):
    list = []
    while node:
        list.append(str(node.data))
        node = node.next
    length = len(list)
    for i in range(int(length / 2)):
        if list[i] != list[length - 1 - i]:
            return False
    return True

node1 = createLinkedListFromArray([1,2,3,3,2,1])
node2 = createLinkedListFromArray([1,2,3,4,5,6])
node3 = createLinkedListFromArray([1,2,3,3,3,2,1])
node4 = createLinkedListFromArray(['a','b','c','d','e','f'])
node5 = createLinkedListFromArray(['a','b','zzz','b','a'])
node6 = createLinkedListFromArray([0])
testCases = [node1, node2, node3, node4, node5, node6]
expectedResults = [True, False, True, False, True, True]
testFunction(testCases, expectedResults, isPalindrome)

