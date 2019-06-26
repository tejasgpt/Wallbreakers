class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        PROBLEM STATEMENT:
        A self-dividing number is a number that is divisible by every digit it contains.
        Given a lower and upper number bound, output a list of every possible self dividing number, 
        including the bounds if possible. 
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def selfDividingNumber(num):
            for digit in str(num):
                if digit == "0" or num % int(digit) != 0:
                    return False
            return True
        
        res = []
        for num in range(left, right + 1):
            if selfDividingNumber(num):
                res.append(num)
        return res
