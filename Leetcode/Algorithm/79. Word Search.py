from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, i):
            if (i == len(word)):
                return True
            
            for dr, dc in dirs:
                newR, newC = r + dr, c + dc

                if (newR < 0 or newR >= m or newC < 0 or newC >= n):
                    continue
                
                if ((newR, newC) in visited):
                    continue
                
                if (board[newR][newC] != word[i]):
                    continue
                
                visited.add((newR, newC))

                if (dfs(newR, newC, i + 1)):
                    return True
                
                visited.remove((newR, newC))
            
            return False
        
        for r in range(m):
            for c in range(n):
                if (board[r][c] == word[0]):
                    visited = set([(r, c)])

                    if (dfs(r, c, 1)):
                        return True
        
        return False
    
"""
Time Complexity: O(M * N * 3^K)
Space Complexity: O(K)

Where
M = number of rows in matrix board
N = number of columns in matrix board
K = length of string word
"""