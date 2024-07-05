# Description
# Given two strings, write a method to decide if one is a permutation of the other.

# Note:
# This solution only applies for languages with a Latin alphabet, other languages that use different character sets (like unicode) are not contemplated here.

from testing_functions import testFunction

def normalizeCase(text):
	return text.lower()

def isPremutationTest(texts):
	text1 = normalizeCase(texts[0])
	text2 = normalizeCase(texts[1])
	return isPermutation(text1, text2)

def isPermutation(text1, text2):
	if len(text1) != len(text2):
		return False
	maxCharAsciiRawRepresentation = 127 # includes letters, space, numbers and common punctuation marks
	charCount = [0] * maxCharAsciiRawRepresentation
	for char in text1:
		charCount[ord(char)] += 1
	for char in text2:
		charCount[ord(char)] -= 1
	return all(count == 0 for count in charCount)

testCases = [['hola', 'aloh'], ['Anita lava la tina', 'latina lava a nita'], ['pepito', 'petite'], ['hello ', 'hello']]
expectedResults = [True, True, False, False]
testFunction(testCases, expectedResults, isPremutationTest)