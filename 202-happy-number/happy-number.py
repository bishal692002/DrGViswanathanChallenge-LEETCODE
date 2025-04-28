class Solution(object):
    def isHappy(self, n):
        if n == 1 or n == 7: return True
        elif n < 10: return False

        s = 0
        while n > 0:
            r = n % 10
            s += r ** 2 
            n = n // 10
        
        return self.isHappy(s)
        
        