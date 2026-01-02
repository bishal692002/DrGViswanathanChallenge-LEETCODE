class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            com = target - nums[i]
            if com in seen:
                return [seen[com], i]
            seen[nums[i]] = i
