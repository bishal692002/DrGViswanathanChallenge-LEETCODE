import math

class Solution(object):
    def uniquePaths(self, m, n):
        return math.factorial(m + n - 2) // (math.factorial(m - 1) * math.factorial(n - 1))