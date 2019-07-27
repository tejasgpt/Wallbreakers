# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        PROBLEM STATEMENT:
        Find the sum of all left leaves in a given binary tree.
        :type root: TreeNode
        :rtype: int
        """     
        leftSum = 0
        
        if not root:
            return 0
        
        if root.left and not root.left.left and not root.left.right:
            leftSum += root.left.val
            
        leftSum += self.sumOfLeftLeaves(root.left)
        leftSum += self.sumOfLeftLeaves(root.right)
        
        return leftSum
