# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        PROBLEM STATEMENT:
        Given two binary trees, write a function to check if they are the same or not.
        Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack = [(p, q)]
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            elif not node1 or not node2:
                return False
            else:
                if node1.val != node2.val:
                    return False
                stack.append((node1.left, node2.left))
                stack.append((node1.right, node2.right))
        return True
