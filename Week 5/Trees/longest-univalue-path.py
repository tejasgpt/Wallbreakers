# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        PROBLEM STATEMENT:
        Given a binary tree, find the length of the longest path 
        where each node in the path has the same value. 
        This path may or may not pass through the root.
        The length of path between two nodes is represented by the number of edges between them.
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        def path(node, prev):
            if not node:
                return 0
            
            left = path(node.left, node.val)
            right = path(node.right, node.val)
            
            self.max_val = max(self.max_val, left + right)
            if node.val == prev:
                return max(left, right) + 1
            return 0
        
        self.max_val = 0
        path(root, root.val)
        return self.max_val
