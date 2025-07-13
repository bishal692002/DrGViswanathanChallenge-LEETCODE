class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        csum = 0
        msum = float('-inf')

        for i in range(len(nums)):
            csum += nums[i]
            msum = max(csum,msum)

            if csum<0:
                csum=0
        return msum
