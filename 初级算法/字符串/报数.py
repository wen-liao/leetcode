class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        
        def next(s):
            count = 1
            ret = ''
            for i in range(len(s)):
                if (i < len(s) - 1) and (s[i] == s[i+1]):
                    count += 1
                else:
                    ret += str(count) + s[i]
                    count = 1
            return ret
        
        result = '1'
        for i in range(n-1):
            result = next(result)
        return result