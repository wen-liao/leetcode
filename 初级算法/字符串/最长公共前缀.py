class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        max_len = len(strs[0])
        for i in range(1, len(strs)):
            max_len = min(max_len, len(strs[i]))
            if max_len == 0:
                return ""
            for j in range(max_len):
                if strs[i-1][j] != strs[i][j]:
                    j -= 1
                    break
            max_len = j + 1
        return strs[0][:max_len]