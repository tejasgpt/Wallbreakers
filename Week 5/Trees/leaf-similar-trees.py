# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        PROBLEM STATEMENT:
        Consider all the leaves of a binary tree.  From left to right order, 
        the values of those leaves form a leaf value sequence.
        Two binary trees are considered leaf-similar if their leaf value sequence is the same.
        Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def leaves(root):
            leaf = []
            stack = [root]

            while stack:
                curr = stack.pop()
                if not curr:
                    continue
                if curr and not curr.left and not curr.right:
                    leaf.append(curr.val)
                else:
                    stack.append(curr.left)
                    stack.append(curr.right)
            return leaf
        
        return leaves(root1) == leaves(root2)
