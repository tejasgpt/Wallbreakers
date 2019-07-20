# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        PROBLEM STATEMENT:
        Given a singly linked list, group all odd nodes together followed by the even nodes. 
        Please note here we are talking about the node number and not the value in the nodes.
        Try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: 
            return head
        
        prev, odd, even = head, head.next, head.next
        
        while even and even.next:
            temp = even.next
            prev.next = prev = temp
            even.next = temp.next
            even = even.next
        prev.next = odd
        return head
