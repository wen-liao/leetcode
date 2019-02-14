class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_ = 0
        for val in nums:
            sum_ += val
        return len(nums)*(len(nums)+1)//2 - sum_