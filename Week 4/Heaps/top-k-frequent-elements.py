class Solution(object):
    def topKFrequent(self, nums, k):
        """
        PROBLEM STATEMENT:
        Given a non-empty array of integers, return the k most frequent elements.
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        heap = []
        count = {}
        
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
                
        for key,val in count.items():
            heapq.heappush(heap,(val,key))     
            if len(heap) > k:
                heapq.heappop(heap)
                
        return [element[1] for element in heap]
     
# ALTERNATE SOLUTION

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        PROBLEM STATEMENT:
        Given a non-empty array of integers, return the k most frequent elements.
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
                
        return heapq.nlargest(k, count.keys(), key = count.get)
