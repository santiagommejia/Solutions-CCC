from node import Node

def createLinkedListFromArray(nodes):
    if len(nodes) == 0:
        print('Nodes must have at least one item')
    head = Node(nodes[0])
    for i in range(1, len(nodes)):
        head.append_node_to_tail(Node(nodes[i]))
    return head

def createLinkedListFromNodes(nodes):
    if len(nodes) == 0:
        print('Nodes must have at least one item')
    head = nodes[0]
    for i in range(1, len(nodes)):
        head.append_node_to_tail(nodes[i])
    return head

def printLinkedList(head, message=''):
    nodes = []
    while head:
        nodes.append(head.data)
        head = head.next
    print(message, nodes)

def testFunction(testCases, expectedResults, testFunction):
	if len(testCases) != len(expectedResults):
		print('testCases must have the same length as expectedResuls')
		return False
	allTestCasesPassed = True
	for i in range(0, len(testCases)):
		result = testFunction(testCases[i])
		if result != expectedResults[i]:
			print('Failed on test case:', i, testCases[i])
			print('Returned:', result)
			print('Expected:', expectedResults[i])
			allTestCasesPassed = False
			break
	if allTestCasesPassed:
		print('All test cases passed')
