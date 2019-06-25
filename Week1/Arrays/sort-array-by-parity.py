class Solution(object):
    def sortArrayByParity(self, A):
        """
        PROBLEM STATEMENT:
        Given an array A of non-negative integers, 
        return an array consisting of all the even elements of A, 
        followed by all the odd elements of A.
        :type A: List[int]
        :rtype: List[int]
        """
        left, right = 0, len(A) - 1
        while left < right:
            if A[left] % 2 != 0:
                if A[right] % 2 == 0:
                    A[left], A[right] = A[right], A[left]
                else:
                    right -= 1
            else:
                left += 1
        return A
