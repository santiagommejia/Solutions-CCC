# Problem Description
# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

from testing_functions import printMatrix

def rotateMatrix(matrix, N):
	rotatedMatrix = [[0 for _ in range(N)] for _ in range(N)]
	for x in range(N):
		for y in range(N):
			xf = y
			yf = N - x - 1
			rotatedMatrix[xf][yf] = matrix[x][y]
	return rotatedMatrix 

def rotateMatrixInPlace(matrix, N):
	replacedSquaresDict = {}
	for x in range(N):
		for y in range(N):
			xf = y
			yf = N - x - 1
			if (xf, yf) not in replacedSquaresDict:
				holder = matrix[x][y]
				for _ in range(N):
					temp = matrix[xf][yf]
					matrix[xf][yf] = holder
					holder = temp
					replacedSquaresDict[(xf, yf)] = True
					tempX = xf
					xf = yf
					yf = N - tempX - 1
			else:
				continue
	return matrix

N = 5
testMatrix = [[y + N*x for y in range(1, N + 1)] for x in range(N)]
print('original: ')
printMatrix(testMatrix)
print('rotated: ')
printMatrix(rotateMatrix(testMatrix, N))
print('inplace: ')
printMatrix(rotateMatrixInPlace(testMatrix, N))


