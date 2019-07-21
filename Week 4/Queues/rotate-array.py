class Solution(object):
    def rotate(self, nums, k):
        """
        PROBLEM STATEMENT:
        Given an array, rotate the array to the right by k steps, where k is non-negative.
        """
        queue = collections.deque(nums)
        k %= len(nums)
        i = 0
        while i < k:
            queue.appendleft(queue.pop())
            i += 1
        nums[:] = list(queue)
