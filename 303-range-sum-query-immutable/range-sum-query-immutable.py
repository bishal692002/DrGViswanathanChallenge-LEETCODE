import array as arr
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix_sumNums = [0]
        running_sum = 0

        for i in nums:
            running_sum += i
            self.prefix_sumNums.append(running_sum) 

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        sumFinal = self.prefix_sumNums[right + 1 ] - self.prefix_sumNums[left]
        return sumFinal


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)