class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for num in set(nums):
            if num > 0:
                ans += num

        return ans if ans else max(nums)