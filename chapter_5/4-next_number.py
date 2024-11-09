# Description
# Given a positive integer, print the next smallest and the next largest number that have the same number of 1 bits in their binary representation.
from testing_functions import testFunction

def getNextBiggest(num):
  numCopy = num
  lsb = numCopy & 1
  rightSeqCounter = 0
  while numCopy != 0:
    if lsb == numCopy & 1:
      rightSeqCounter += 1
    else:
      break
    numCopy >>= 1
  return num + 2**(rightSeqCounter - lsb)

def getNextSmallest(num):
  numCopy = num
  zeroFound = False
  rightCount = 0
  while numCopy != 0:
    if zeroFound and numCopy & 1 == 1:
      break
    zeroFound = zeroFound or numCopy & 1 == 0
    numCopy >>= 1
    rightCount += 1
  if not zeroFound:
    return round(num / 2, 1)
  else:
    num = num & ~(1 << rightCount)
    return num | (1 << rightCount -1)


testCasesNextBiggest = [743, 15, 11, 5, 1]
expectedResultsNextBiggest = [747, 23, 13, 6, 2]
testCasesNextSmallest = [743, 8, 15, 31, 21]
expectedResultsNextSmallest = [727, 4, 7.5, 15.5, 19]
testFunction(testCasesNextBiggest, expectedResultsNextBiggest, getNextBiggest)
testFunction(testCasesNextSmallest, expectedResultsNextSmallest, getNextSmallest)
