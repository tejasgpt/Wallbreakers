class Solution(object):
    def numIslands(self, grid):
        """
        PROBLEM STATEMENT:
        Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
        An island is surrounded by water and is formed by connecting adjacent lands 
        horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(grid, row, col):
            if grid[row][col] == '0':
                return
            grid[row][col] = '0'

            if row != 0:
                dfs(grid, row - 1, col)
            if row != len(grid) - 1:
                dfs(grid, row + 1, col)
            if col != 0:
                dfs(grid, row, col - 1)
            if col != len(grid[0]) - 1:
                dfs(grid, row, col + 1)
                
        if not grid:
            return 0

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    islands += 1
        return islands
