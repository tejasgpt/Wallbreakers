class Solution(object):
    def findErrorNums(self, nums):
        """
        PROBLEM STATEMENT:
        Given an array nums representing the data status of this set after the error. 
        Your task is to firstly find the number occurs twice and then find the number that is missing. 
        Return them in the form of an array.
        :type nums: List[int]
        :rtype: List[int]
        """
        import collections
        n = collections.Counter(nums)
        mismatch = []
        for digit, count in n.items():
            if count == 2:
                mismatch.append(digit)
        mismatch.append(sum(range(1,len(nums)+1)) - sum(nums) + mismatch[0])
        return mismatch
