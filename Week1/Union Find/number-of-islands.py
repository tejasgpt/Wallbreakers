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
        if len(grid) == 0: 
            return 0
        row, col = len(grid), len(grid[0])
        self.count = sum(grid[i][j]=='1' for i in range(row) for j in range(col))
        parent = [i for i in range(row*col)]
        
        def find(x):
            if parent[x]!= x:
                return find(parent[x])
            return parent[x]
        
        def union(x,y):
            xroot, yroot = find(x),find(y)
            if xroot == yroot: return 
            parent[xroot] = yroot
            self.count -= 1
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    continue
                index = i*col + j
                if j < col-1 and grid[i][j+1] == '1':
                    union(index, index+1)
                if i < row-1 and grid[i+1][j] == '1':
                    union(index, index+col)
        return self.count
    
# Alternate Solution usin DFS
    
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
