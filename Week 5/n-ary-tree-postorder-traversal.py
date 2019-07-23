"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        PROBLEM STATEMENT:
        Given an n-ary tree, return the postorder traversal of its nodes' values.
        :type root: Node
        :rtype: List[int]
        """
        nary = []
        if not root: 
            return nary

        stack = [root]
        
        while stack:
            curr = stack.pop()
            nary.append(curr.val)
            stack.extend(curr.children)
            
        return nary[::-1]
