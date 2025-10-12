class Solution(object):
    def smallestEqual(self, nums):
        cnt = 0
        ind = 0
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                cnt += 1
                if not ind:
                    ind = i
                    break
        if not cnt:
            return - 1
        else:
            return ind    