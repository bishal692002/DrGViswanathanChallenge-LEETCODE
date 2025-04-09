class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        while len(nums) != len(set(nums)):
            nums = nums[3:]
            count += 1
        return count


