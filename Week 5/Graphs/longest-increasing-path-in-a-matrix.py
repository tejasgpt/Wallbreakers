class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        PROBLEM STATEMENT:
        Given an integer matrix, find the length of the longest increasing path.
        From each cell, you can either move to four directions: left, right, up or down. 
        You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
        :type matrix: List[List[int]]
        :rtype: int
        """
        def path(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    path(i - 1, j) if i > 0 and val > matrix[i - 1][j] else 0,
                    path(i + 1, j) if i < row - 1 and val > matrix[i + 1][j] else 0,
                    path(i, j - 1) if j > 0 and val > matrix[i][j - 1] else 0,
                    path(i, j + 1) if j < col - 1 and val > matrix[i][j + 1] else 0)
            return dp[i][j]
    
        if not matrix or not matrix[0]: 
            return 0
        
        row, col = len(matrix), len(matrix[0])
        dp = [[0] * col for i in range(row)]
        
        return max(path(x, y) for x in range(row) for y in range(col))
