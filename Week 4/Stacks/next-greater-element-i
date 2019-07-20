class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        PROBLEM STATEMENT:
        You are given two arrays (without duplicates) nums1 and nums2 
        where nums1’s elements are subset of nums2. 
        Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
        The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. 
        If it does not exist, output -1 for this number.
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = list()
        great = dict()
        
        for num in nums2:
            while stack != [] and num > stack[-1]:
                great[stack.pop()] = num
            stack.append(num)
            
        nxt = []
        
        for num in nums1:
            if num in great:
                nxt.append(great[num])
            else:
                nxt.append(-1)
        return nxt
