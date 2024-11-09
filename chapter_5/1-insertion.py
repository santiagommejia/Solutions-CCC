# Description
# You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method to insert M into N such that M starts at bit j and ends at bit i. You can assume that the bits j through i have enough space to fit all of M. That is, if M = 10011, you can assume that there are at least 5 bits between j and i. You would not, for example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.
# EXAMPLE
# Input: N = 10000000000, M = 10011, i = 2, j = 6
# Output: N = 10001001100

from testing_functions import testFunction

def insertion(n, m, i, j):
  mBitMask = m << i
  cleaningMask = (1 << 32) - 1
  cleaningMask <<= i + j - 1
  cleaningMask |= (1 << i) - 1
  n &= cleaningMask
  return n | mBitMask

def testInsertion(args):
  return insertion(args[0], args[1], args[2], args[3])


n = 0b10000000000
m = 0b10011
m2 = 0b11011
m3 = 0b11111
i = 2
j = 6
testCases = [[n,m,i,j], [n,m2,i,j], [n,m3,i,j]]
expectedResults = [0b10001001100, 0b10001101100, 0b10001111100]
testFunction(testCases, expectedResults, testInsertion)