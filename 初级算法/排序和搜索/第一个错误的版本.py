# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def find(self,begin,end):
        if begin == end:
            return begin
        mid = (begin+end)//2
        if isBadVersion(mid):
            return self.find(begin,mid)
        else:
            return self.find(mid+1,end)
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.find(1,n)