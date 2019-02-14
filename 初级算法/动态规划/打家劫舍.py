class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret,steal,not_steal = 0,0,0
        for i in range(len(nums)):
            steal,not_steal = not_steal + nums[i], max(steal,not_steal)
            ret = max(ret,steal,not_steal)
        return ret