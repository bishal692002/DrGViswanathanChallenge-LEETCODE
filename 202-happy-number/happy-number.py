class Solution(object):
    def isHappy(self, n):
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            s = 0
            while n > 0:
                r = n % 10
                s += r ** 2
                n = n // 10
            n = s
        
        return n == 1
