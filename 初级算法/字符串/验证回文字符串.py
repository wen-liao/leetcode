class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = [char for char in s if char.isalnum()]
        for i in range(len(s)//2):
            if s[i] != s[-(i+1)]:
                return False
        return True