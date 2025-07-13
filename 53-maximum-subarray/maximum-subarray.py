class Solution(object):
    def maxSubArray(self, nums):
        maxSum=nums[0]
        currSum=0
        for i in nums:
            currSum+=i
            maxSum=max(currSum,maxSum)
            if currSum <0:
                currSum=0
        return maxSum