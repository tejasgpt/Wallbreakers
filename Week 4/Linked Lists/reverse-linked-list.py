# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        PROBLEM STATEMENT:
        Reverse a singly linked list.
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode('-INF')
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next
        
