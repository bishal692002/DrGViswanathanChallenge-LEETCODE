class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1
                count = max(count, current)
            else:
                current = 0  
        return count
