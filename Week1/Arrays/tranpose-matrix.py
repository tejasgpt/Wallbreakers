class Solution(object):
    def transpose(self, A):
        """
        PROBLEM STATEMENT:
        Given a matrix A, return the transpose of A.
        The transpose of a matrix is the matrix flipped over it's main diagonal, 
        switching the row and column indices of the matrix.
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        transpose = []
        temp = []
        row = len(A)
        col = len(A[0])
        ind = 0
        for i in range(col):
            for j in range(row):
                temp.append(A[j][i])
            transpose.append(temp)
            temp = []
        return transpose
        
# Alternate Solution

class Solution(object):
    def transpose(self, A):
        """
        PROBLEM STATEMENT:
        Given a matrix A, return the transpose of A.
        The transpose of a matrix is the matrix flipped over it's main diagonal, 
        switching the row and column indices of the matrix.
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
