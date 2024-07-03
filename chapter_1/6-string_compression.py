# Problem Description:
# Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the compressed string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a-z).

from testing_function import testFunction

def stringCompression(text):
	if len(text) <= 2:
		return text
	sameCharCount = 1
	compressedText = ''
	for i in range(1, len(text)):
		isRepeatedChar = text[i] == text[i-1]
		if not isRepeatedChar:
			compressedText += text[i-1] + str(sameCharCount)
		sameCharCount = sameCharCount + 1 if isRepeatedChar else 1
	compressedText += text[len(text) - 1] + str(sameCharCount)
	return text if len(compressedText) > len(text) else compressedText

testCases = ['aabcccccaaa','abcde','hhhhh', 'rrryyyuuui']
expectedResults = ['a2b1c5a3', 'abcde', 'h5', 'r3y3u3i1']
testFunction(testCases, expectedResults, stringCompression)