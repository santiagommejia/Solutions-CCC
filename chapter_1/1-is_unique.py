# Problem Description:
# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

# Note:
# This solution only applies for languages with a Latin alphabet, other languages that use different character sets (like unicode) are not contemplated here.

from testing_functions import testFunction

def normalizeCase(text):
    return text.lower()

# with set
def hasUniqueChars(text):
	text = normalizeCase(text)
	existingChars = set()
	for char in text:
		if char in existingChars:
			return False
		else:
			existingChars.add(char)
	return True

# with array only
def hasUniqueChars(text):
	text = normalizeCase(text)
	maxCharAsciiRawRepresentation = 127 # includes letters, space, numbers and common punctuation marks
	charCount = [0] * maxCharAsciiRawRepresentation
	for char in text:
		asciiValueIndex = ord(char)
		if charCount[asciiValueIndex] > 0:
			return False
		else: 
			charCount[asciiValueIndex] = 1
	return True

# testing
testCases = ['hola','holaque','holaquehace', 'Aloha']
expectedResults = [True, True, False, False]
testFunction(testCases, expectedResults, hasUniqueChars)
