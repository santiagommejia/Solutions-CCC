# Problem Description:
# Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.

# Example:
# Input: "Mr John Smith    ", 13
# Output: "Mr%20John%20Smith"

from testing_function import testFunction

def URLify(text):
	text = text.strip()
	result = ''
	for char in text:
		result += '%20' if ord(char) == 32 else char
	return result

testCases = ['Hello friend', 'what are you doing', 'youare awesome ','    ', 'Mr John Smith    ']
expectedResults = ["Hello%20friend", 'what%20are%20you%20doing', 'youare%20awesome', '', 'Mr%20John%20Smith']
testFunction(testCases, expectedResults, URLify)