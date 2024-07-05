# Problem Description
# Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat").

from testing_functions import testFunction

# is s2 a rotation of s1?
def isSubString(string, substring):
	return substring in string

def isStringRotation(s1, s2):
	return False if len(s1) != len(s2) else isSubString(s2 + s2, s1)

def testIsStringRotation(texts):
	return isStringRotation(texts[0], texts[1])

testCases = [['erbottlewat', 'waterbottle'], ['erbottleswat', 'waterbottle'], ['pipe', 'pepi'], ['pipe', 'piep'], ['pipe', 'ipep']]
expectedResults = [True, False, True, False, True]
testFunction(testCases, expectedResults, testIsStringRotation)


