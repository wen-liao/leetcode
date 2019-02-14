class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dic = {")":"(","]":"[","}":"{"}
        for char in s:
            if char not in dic:
                stack.append(char)
            else:
                if not (len(stack) > 0 and stack.pop() == dic[char]):
                    return False
        return len(stack) == 0