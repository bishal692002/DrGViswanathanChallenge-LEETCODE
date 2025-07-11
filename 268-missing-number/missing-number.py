class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        formula = n * (n+1)//2
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
        return formula - summ
        