class Solution(object):
    def isValidSudoku(self, board):
        """
        PROBLEM STATEMENT:
        Determine if a 9x9 Sudoku board is valid. 
        Only the filled cells need to be validated according to the following rules:
        1. Each row must contain the digits 1-9 without repetition.
        2. Each column must contain the digits 1-9 without repetition.
        3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
        :type board: List[List[str]]
        :rtype: bool
        """
        rowset = [set() for _ in range(9)]
        colset = [set() for _ in range(9)]
        boxset = {"00":set(),"01":set(),"02":set(),"10":set(),"11":set(),"12":set(),"20":set(),"21":set(),"22":set()}
        
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                    
                digit = board[i][j]
                
                if digit in rowset[i] or digit in colset[j] or digit in boxset[str(i//3)+str(j//3)]:
                    return False
                else:
                    rowset[i].add(digit)
                    colset[j].add(digit)
                    boxset[str(i//3)+str(j//3)].add(digit)
                    
        return True
            
                
