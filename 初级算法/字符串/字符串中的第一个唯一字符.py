class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        for char in s:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1