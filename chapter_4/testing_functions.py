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