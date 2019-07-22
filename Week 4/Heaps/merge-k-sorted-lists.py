# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        PROBLEM STATEMENT:
        Merge k sorted linked lists and return it as one sorted list. 
        Analyze and describe its complexity.
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        merge = ListNode('-inf')
        
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                
        node = merge
        
        while heap:
            ind = heapq.heappop(heap)[1]
            node.next = lists[ind]
            node = node.next
            lists[ind] = node.next
            if node.next:
                heapq.heappush(heap, (node.next.val, ind))
                node.next = '-inf'
                
        return merge.next
