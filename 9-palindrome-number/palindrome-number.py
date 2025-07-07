class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        summ = 0
        num = x
        if x < 0:
            return False
        while x != 0:
            di = x % 10  
            summ = summ * 10 + di
            x //= 10
        return summ == num