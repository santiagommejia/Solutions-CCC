# Problem Description
# Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco cta", etc.)

from testing_functions import testFunction

def normalizeCase(text):
	return text.lower()

def isPalindromePermutation(text):
	text = normalizeCase(text)
	charCountDict = {}
	for char in text:
		if char != ' ':
			charCountDict[char] = charCountDict.get(char, 0) + 1
	return sum(charCount % 2 for charCount in charCountDict.values()) <= 1

testCases = ['Tact Coa', 'taco cat', 'anita lava la tina', 'anita lava latina', 'oruro', 'xxyyzx','not a palindrome surely']
expectedResults = [True, True, True, True, True, False, False]
testFunction(testCases, expectedResults, isPalindromePermutation)