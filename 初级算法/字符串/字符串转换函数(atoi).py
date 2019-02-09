class Solution:
    def myAtoi(self, string):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = (1<<31) - 1
        INT_MIN = -(1<<31)
        string = string.strip()
        N = len(string)
        if N == 0:
            return 0
        sign = 1
        value = 0
        i = 0
        if string[0] == '-':
            if len(string) > 1 and string[1].isdigit():
                sign = -1
                i += 1
            else:
                return 0
        elif string [i] == '+':
            if len(string) > 1 and string[1].isdigit():
                i += 1
            else:
                return 0
        while i < N:
            if string[i].isdigit():
                value = value*10 + int(string[i])
                i += 1
                if value > INT_MAX:
                    break
            else:
                break
        value *= sign
        if value < INT_MIN:
            return INT_MIN
        if value > INT_MAX:
            return INT_MAX
        return value