# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def compare(self,root1, root2):
        if root1 == None and root2 == None:
            return True
        if (root1 == None and root2 != None) or (root1 != None and root2 == None):
            return False
        if root1.val != root2.val:
            return False
        if self.compare(root1.left,root2.right) and self.compare(root1.right, root2.left):
            return True
        return False
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.compare(root,root)