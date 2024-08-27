# Problem Description
# Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.

def getMinimalBST(sortedArray, tree, parent = None):
    length = len(sortedArray)
    if length == 1:
        return tree, sortedArray[0]
    elif length == 2:
        if parent is None:
            tree[sortedArray[1]] = [sortedArray[0]]
        else:
            tree[sortedArray[1]] = (tree[sortedArray[1]] if sortedArray[1] in tree else []) + [sortedArray[0]]
        return tree, sortedArray[1]
    halfIndex = int(length / 2)
    halfEl = sortedArray[halfIndex]
    tree, left = getMinimalBST(sortedArray[0: halfIndex], tree, halfEl)
    tree, right = getMinimalBST(sortedArray[halfIndex+1: length], tree, halfEl)
    tree[halfEl] = [left, right]
    return tree, halfEl

sortedArr = [i for i in range(1,19)]
bst, root = getMinimalBST(sortedArr, {})
print('bst:', bst)
print('root:', root)