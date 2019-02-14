class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        priority = {"I":0,"V":1,"X":2,"L":3,"C":4,"D":5,"M":6}
        value = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        ret = 0
        for i in range(len(s)):
            if i < len(s)-1 and priority[s[i]]<priority[s[i+1]]:
                ret -= value[s[i]]
            else:
                ret += value[s[i]]
        return ret