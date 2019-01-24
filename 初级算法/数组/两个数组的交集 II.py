class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1 = {}
        dict2 = {}
        for num in nums1:
            if num in dict1:
                dict1[num] += 1
            else:
                dict1[num] = 1
        for num in nums2:
            if num in dict2:
                dict2[num] += 1
            else:
                dict2[num] = 1
        common = dict1.keys() & dict2.keys()
        ret = []
        for val in common:
            ret += [val] * min(dict1[val],dict2[val])
        return ret