# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def build(self, nums, index, root):
        if index > 0:
            l_index = index // 2
            root.left = TreeNode(nums[l_index])
            self.build(nums[:index],l_index,root.left)
        else:
            root.left = None
        if index < len(nums) - 1:
            r_index = (len(nums) - 1 - index) // 2
            root.right = TreeNode(nums[r_index + index + 1])
            self.build(nums[index+1:],r_index,root.right)
        else:
            root.right = None
            
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        index = len(nums) // 2
        self.ret = TreeNode(nums[index])
        self.build(nums, index, self.ret)
        return self.ret