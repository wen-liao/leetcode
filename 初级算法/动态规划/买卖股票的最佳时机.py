class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        least = prices[0]
        ret = 0
        for i in range(len(prices)):
            least = min(least,prices[i])
            ret = max(ret,prices[i] - least)
        return ret