# Problem Description:
# There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

# Example:
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false

from testing_functions import testFunction

def testIsOneAway(texts):
	return isOneAway(texts[0], texts[1])

def isOneAway(text1, text2):
	awayCount = 0
	len1 = len(text1)
	len2 = len(text2)
	if len1 == len2:
		for i in range(len1):
			awayCount += 1 if text1[i] != text2[i] else 0
			if awayCount > 1:
				return False
	else:
		shortText = text1 if len1 < len2 else text2
		longText = text1 if len1 > len2 else text2
		shortTextIterator = 0
		while shortTextIterator < len(shortText):
			isDifferent = shortText[shortTextIterator] != longText[shortTextIterator + awayCount]
			shortTextIterator += 1 if not isDifferent else 0
			awayCount += 1 if isDifferent else 0
			if awayCount > 1:
				return False
	return True

testCases = [['pale', 'ple'],['pales', 'pale'], ['pale', 'bale'], ['xpale', 'bale'], ['pale', 'bake']]
expectedResults = [True, True, True, False, False]
testFunction(testCases, expectedResults, testIsOneAway)