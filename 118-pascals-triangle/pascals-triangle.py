class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for n in range(numRows):
            row = [1]
            num = 1
            for i in range(1, n + 1):
                num *= (n - i + 1)
                num //= i
                row.append(num)
            result.append(row)
        return result
