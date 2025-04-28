class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hihi = set(nums)
        hello = []
        
        for i in range(1, len(nums) + 1):
            if i not in hihi:
                hello.append(i)
        return hello
