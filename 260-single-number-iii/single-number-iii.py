class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hello= []
        dicti = {}
        for num in nums:
            if num in dicti:
                dicti[num] += 1
            else:
                dicti[num] = 1
        for key, value in dicti.items():
            if value == 1:
                hello.append(key)
        return hello
        