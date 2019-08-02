class Solution(object):
    def merge(self, intervals):
        """
        PROBLEM STATEMENT:
        Given a collection of intervals, merge all overlapping intervals.
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        
        
        intervals.sort()
        
        n = len(intervals)
        start = end = intervals[0][0]
        
        merged = []
        i = 0
        while end < intervals[n-1][1]:
            if i < n and end >= intervals[i][0]:
                while i < n and end >= intervals[i][0]:
                    end = max(end, intervals[i][1])
                    i += 1
            else:
                merged.append([start,end])
                start = end = intervals[i][0]
                
        merged.append([start,end])
        return merged
        
