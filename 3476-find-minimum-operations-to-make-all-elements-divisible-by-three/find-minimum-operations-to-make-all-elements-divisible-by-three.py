class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0 
        for num in nums:
            if num % 3 == 1 or num % 3 == 2:
                count += 1
        return count
        