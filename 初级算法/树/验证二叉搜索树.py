# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def traversal(self,root):
        if not root.left == None:
            self.traversal(root.left)
        self.elements.append(root.val)
        if not root.right == None:
            self.traversal(root.right)
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.elements = []
        if root == None:
            return True
        self.traversal(root)
        for i in range(len(self.elements)-1):
            if self.elements[i] >= self.elements[i+1]:
                return False
        return True