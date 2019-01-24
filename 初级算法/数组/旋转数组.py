class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if (len(nums) == 0) or (k == 0):
            return
        #gcd(len(nums),k)
        gcd,temp = len(nums),k
        while (gcd != 0) and (temp != 0):
            if gcd > temp:
                gcd %= temp
            else:
                temp %= gcd
        if gcd == 0:
            gcd = temp
                
        def switch(ix,k,nums):
            temp = nums[ix]
            N = len(nums)
            nums[ix] = nums[(ix + N - k)%N]
            j = (ix + N - k)%N
            while j != ix:
                nums[j] = nums[(j + N - k)%N]
                j = (j + N - k)%N
            nums[(ix + k)%N] = temp
        
        for i in range(gcd):
            switch(i,k,nums)