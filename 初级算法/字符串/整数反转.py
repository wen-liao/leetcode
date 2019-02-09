class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MIN = -(1<<31)
        MAX = (1<<31)-1
        sign = 1
        if x == 0:
            return 0
        if x < 0:
            sign = -1
            x = -x
        ret = 0
        while x > 0:
            ret = ret*10 + x%10
            x //= 10
        ret *= sign
        if MIN <= ret <= MAX:
            return ret
        else:
            return 0