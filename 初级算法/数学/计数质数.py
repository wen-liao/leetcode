class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1 or n == 2:
            return 0
        rec = [1]*n
        rec[0],rec[1] = 0,0
        count = 0
        for i in range(2,n):
            if rec[i] == 1:
                count += 1
                j = 2*i
                while j < n:
                    rec[j] = 0
                    j += i
        return count