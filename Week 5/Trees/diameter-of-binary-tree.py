# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        PROBLEM STATEMENT:
        Given a binary tree, you need to compute the length of the diameter of the tree. 
        The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
        This path may or may not pass through the root.
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        self.diameter = 0
        self.depth(root)
        return self.diameter - 1
    
    def depth(self, node):
        if not node:
            return 0
        
        left = self.depth(node.left)
        right = self.depth(node.right)
        
        self.diameter = max(self.diameter, left + right + 1)
            
        return max(left, right) + 1
