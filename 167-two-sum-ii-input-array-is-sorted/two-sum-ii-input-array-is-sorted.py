class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left,right = 0,len(numbers)-1
        while left<right:
            csum = numbers[left] + numbers[right]
            if csum == target:
                return [left+1,right+1]
            elif csum < target:
                left = left + 1
            else:
                right = right - 1                   
        