class Solution(object):
    def plusOne(self, digits):
        """
        PROBLEM STATEMENT:
        Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
        :type digits: List[int]
        :rtype: List[int]
        """
        size = len(digits) - 1
        while digits[size] == 9:
            digits[size] = 0
            size -= 1
        if size < 0:
            digits = [1] + digits
        else:
            digits[size] += 1
        return digits
