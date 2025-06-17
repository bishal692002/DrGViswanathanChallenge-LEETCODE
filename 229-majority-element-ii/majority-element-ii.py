class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hmap = {}
        for num in nums:
            if num in hmap:
                hmap[num] += 1
            else:
                hmap[num] = 1
        result = []
        for key,value in hmap.items():
            if value > len(nums)//3:
                result.append(key)
        return result
        