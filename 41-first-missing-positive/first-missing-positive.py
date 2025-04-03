class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sett = set()
        for num in nums:
            if num > 0:
                sett.add(num)
        
        missing = 1
        while missing in sett:
            missing += 1
        return missing