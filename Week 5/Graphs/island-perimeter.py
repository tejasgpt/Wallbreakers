# Solution in O(mn) time 

class Solution(object):
    def islandPerimeter(self, grid):
        """
        PROBLEM STATEMENT:
        You are given a map in form of a two-dimensional integer grid 
        where 1 represents land and 0 represents water.
        Grid cells are connected horizontally/vertically (not diagonally). 
        The grid is completely surrounded by water, and there is exactly one island 
        (i.e., one or more connected land cells).
        The island doesn't have "lakes" (water inside that isn't connected to the water around the island).
        One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
        Determine the perimeter of the island.
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col, perimeter = len(grid), len(grid[0]), 0
        for m in range(row):
          for n in range(col):
            if grid[m][n] == 1:
              if m == 0   or grid[m-1][n] == 0: perimeter += 1
              if n == 0   or grid[m][n-1] == 0: perimeter += 1
              if n == col-1 or grid[m][n+1] == 0: perimeter += 1
              if m == row-1 or grid[m+1][n] == 0: perimeter += 1
        return perimeter
