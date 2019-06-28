class Solution(object):
    def solve(self, board):
        """
        PROBLEM STATEMENT:
        Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
        A region is captured by flipping all 'O's into 'X's in that surrounded region.
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def dfs(i, j, m, n, board):
            if i > 0 and board[i - 1][j] == 'O':
                board[i - 1][j] = 'S'
                dfs(i - 1, j, m, n, board)

            if i < m - 1 and board[i + 1][j] == 'O':
                board[i + 1][j] = 'S'
                dfs(i + 1, j, m, n, board)

            if j > 0 and board[i][j - 1] == 'O':
                board[i][j - 1] = 'S'
                dfs(i, j - 1, m, n, board)

            if j < n - 1 and board[i][j + 1] == 'O':
                board[i][j + 1] = 'S'
                dfs(i, j + 1, m, n, board)
                
        if not board:
            return
        
        m, n = len(board), len(board[0])
        
        for i, row in enumerate(board):
            index = range(n) if i == 0 or i == m - 1 else [0, n - 1]
            for j in index:
                if row[j] == 'O':
                    row[j] = 'S'
        
        for i, row in enumerate(board):
            index = range(n) if i == 0 or i == m - 1 else [0, n - 1]
            for j in index:
                if row[j] == 'S':
                    dfs(i, j, m, n, board)
        
        for row in board:
            for j in range(n):
                row[j] = 'O' if row[j] == 'S' else 'X'
                
        return board
