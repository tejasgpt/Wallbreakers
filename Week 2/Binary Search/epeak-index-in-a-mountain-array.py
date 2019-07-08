class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        PROBLEM STATEMENT:
        Given an array that is definitely a mountain, return any i 
        such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].
        :type A: List[int]
        :rtype: int
        """
        left, right = 0, len(A) - 1
        while True:
            mid = (left + right)//2
            if A[mid-1] < A[mid] > A[mid+1]:
                return mid
            elif A[mid-1] < A[mid] < A[mid+1]:
                left = mid + 1
            else:
                right = mid - 1
