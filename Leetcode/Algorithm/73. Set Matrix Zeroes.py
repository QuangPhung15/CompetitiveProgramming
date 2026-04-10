from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rowZero, colZero = False, False

        for i in range(m):
            for j in range(n):
                if (matrix[i][j] == 0):
                    matrix[i][0] = 0
                    matrix[0][j] = 0

                    if (i == 0):
                        rowZero = True
                    if (j == 0):
                        colZero = True
        
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if (matrix[i][0] != 0 and matrix[0][j] != 0):
                    continue
                
                if (i > 0 and j > 0):
                    matrix[i][j] = 0
                elif (i == 0 and rowZero):
                    matrix[i][j] = 0
                elif (j == 0 and colZero):
                    matrix[i][j] = 0

"""
Time Complexity: O(M * N)
Space Complexity: O(1)

Where
M = the number of rows in matrix matrix
N = the number of columns in matrix matrix
"""