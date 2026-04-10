from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])
        l, r = 0, ROW - 1

        def binary_search(row):
            l, r = 0, COL - 1

            while (l <= r):
                m = l + (r - l) // 2

                if (matrix[row][m] == target):
                    return True
                elif (matrix[row][m] < target):
                    l = m + 1
                else:
                    r = m - 1
            
            return False

        while (l <= r):
            m = l + (r - l) // 2

            if (matrix[m][0] <= target <= matrix[m][COL - 1]):
                return binary_search(m)
            elif (matrix[m][COL - 1] < target):
                l = m + 1
            else:
                r = m - 1
        
        return False
    
"""
Time Complexity: O(logM + logN) = O(log(M * N))
Space Complexity: O(1)

Where
M = the number of rows in matrix matrix
N = the number of columns in matrix matrix
"""