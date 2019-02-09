# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        depth = 0
        if root.left != None:
            depth = self.maxDepth(root.left)
        if root.right != None:
            ret = self.maxDepth(root.right)
            depth = max(ret,depth)
        return depth + 1