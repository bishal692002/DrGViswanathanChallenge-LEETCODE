class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        small = []
        large = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                small.append(i)
                if i != n // i:
                    large.append(n // i)
        factors = small + large[::-1]
        if k <= len(factors):
            return factors[k - 1]
        else:
            return -1