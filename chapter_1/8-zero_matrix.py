# Problem Description
# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

from testing_function import printMatrix

def zeroMatrix(matrix, rows, cols):
	zeroMat = [[matrix[x][y] for y in range(cols)] for x in range(rows)]
	for x in range(rows):
		for y in range(cols):
			if matrix[x][y] == 0:
				zeroMat[x] = [0 for _ in range(cols)]
				zeroMat[:][y] = 0
				for row in zeroMat:
					row[y] = 0
	return zeroMat


M = 8 # rows
N = 6 # cols
testMatrix = [[x + N*y for x in range(1, N+1)] for y in range(M)]
testMatrix[2][3] = 0
testMatrix[5][1] = 0
print("original:")
printMatrix(testMatrix)
print("zero matrix:")
printMatrix(zeroMatrix(testMatrix, M, N))
