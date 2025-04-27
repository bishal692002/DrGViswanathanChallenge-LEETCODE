class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(1, len(nums) - 1):
            if nums[i] % 2 == 0:  
                if nums[i-1] + nums[i+1] == nums[i] // 2:
                    count += 1
        return count
