class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hello =set()
        for num in nums:
            if num in hello:
                return True
            hello.add(num)
        return False
        
            