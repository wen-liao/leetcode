class Solution:
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """
        n = len(s)//2
        for i in range(n):
            s[i],s[-(i+1)] = s[-(i+1)],s[i]