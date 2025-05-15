class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ns = ""
        for digit in digits:
            ns += str(digit)
        
        num = int(ns) + 1
        
        arr = []
        for n in str(num):
            arr.append(int(n))
        return arr
        