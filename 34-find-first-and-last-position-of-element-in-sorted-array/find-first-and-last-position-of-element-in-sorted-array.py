class Solution(object):
    def searchRange(self, nums, target):
        hello = []

        for i in range(len(nums)):
            if nums[i] == target:
                hello.append(i)
        if len(hello)>0:
                return[hello[0],hello[-1]]
        else:
            return [-1,-1]