# Description
# You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to find the length of the longest sequence of 1s you could create.
# EXAMPLE
# Input: 1775 (or: 11011101111)
# Output: 8

from testing_functions import testFunction

def flipBitToWin(binary):
  currentSeq = 0
  rightSeq = 0
  maxSoFar = 1
  while binary != 0:
    rightBit = binary & 1
    if rightBit == 1:
      currentSeq += 1
    else:
      rightSeq = currentSeq + 1
      currentSeq = 0
    maxSoFar = max(maxSoFar, rightSeq + currentSeq)
    binary >>= 1
  return maxSoFar

testCases = [0b11011101111,0b11111101111, 0b1000001, 0b1011001, 0b1111, 0b0000]
expectedResults = [8, 11, 2, 4, 4, 1]
testFunction(testCases, expectedResults, flipBitToWin)