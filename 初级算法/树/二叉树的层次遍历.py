# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def traversal(self,depth,root):
        if root == None:
            return
        if len(self.ret) <= depth:
            self.ret.append([])
        self.ret[depth].append(root.val)
        self.traversal(depth+1, root.left)
        self.traversal(depth+1,root.right)
    
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.ret = []
        self.traversal(0,root)
        return self.ret