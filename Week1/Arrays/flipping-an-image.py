class Solution(object):
    def flipAndInvertImage(self, A):
        """
        PROBLEM STATEMEMT:
        Given a binary matrix A, we want to flip the image horizontally, 
        then invert it, and return the resulting image.
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            A[i][:] = A[i][::-1] 
            for j in range(len(A[0])):
                A[i][j] = 1 - A[i][j] 
        return A
