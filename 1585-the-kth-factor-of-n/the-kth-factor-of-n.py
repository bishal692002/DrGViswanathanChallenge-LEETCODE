class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        factors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                factors.append(i)
                if n // i != i:
                    factors.append(n // i)
        factors.sort()
        if k <= len(factors):
            return factors[k - 1]
        else:
            return -1