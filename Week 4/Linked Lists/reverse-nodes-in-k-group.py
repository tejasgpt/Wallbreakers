# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        PROBLEM STATEMENT:
        Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
        k is a positive integer and is less than or equal to the length of the linked list. 
        If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <= 1 or not head: 
            return head
        
        count = 0
        curr = head
        
        while curr:
            curr = curr.next
            count += 1
        
        curr, prev = head, None
        
        while True:
            start, end = prev, curr
            
            if count < k: 
                break
                
            i = 0
            
            while curr and i < k:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                i += 1
                count -= 1
                
            if start:
                start.next = prev
            else:
                head = prev
                
            end.next = curr
            
            if not curr: 
                break
            prev = end
                
        return head
