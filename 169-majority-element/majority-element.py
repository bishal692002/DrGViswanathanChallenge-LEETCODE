class Solution(object):
    def majorityElement(self,nums):
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        for key,value in counts.items():
            if value > len(nums)/2:
                return key
        



 