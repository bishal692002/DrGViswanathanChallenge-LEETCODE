class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        hello = []
        for i in nums[:]:
            if i == 0:
                hello.append(0)
                nums.remove(i)

        nums[:] = nums + hello
