# SOLUTION USING HASH MAPS

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        PROBLEM STATEMENT:
        Given two arrays, write a function to compute their intersection.
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        intersection = set()
        n1 = defaultdict(int)
        n2 = defaultdict(int)
        
        for num in nums1:
            n1[num] +=1
        
        for num in nums2:
            if num in n1 and num not in n2:
                intersection.add(num)
                n2[num] = 1
        return sorted(intersection)
        
# ALTERNATE SOLUTION USING HASH SETS

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        PROBLEM STATEMENT:
        Given two arrays, write a function to compute their intersection.
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))
        
 
