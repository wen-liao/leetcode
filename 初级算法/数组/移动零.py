class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        i = -1
        for i in range(N):
            if nums[i] == 0:
                break
        if i < 0:
            return
        j = i + 1
        while j < N:
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
                nums[j] = 0
            j += 1