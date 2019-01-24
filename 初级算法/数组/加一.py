class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #x[N-1-i]
        r = 1
        N = len(digits)
        for i in range(N):
            digits[N-1-i] += r
            r = 0
            if digits[N-1-i] > 9:
                digits[N-1-i] -= 10
                r = 1
            else:
                break
        if r == 1:
            digits = [1] + digits
        return digits