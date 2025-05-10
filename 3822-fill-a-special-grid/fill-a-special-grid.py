class Solution(object):
    def specialGrid(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        def build(n, start):
            if n == 0:
                return [[start]]

            size = 2 ** (n - 1)
            q1 = build(n - 1, start)
            q2 = build(n - 1, start + size * size)
            q3 = build(n - 1, start + 2 * size * size)
            q4 = build(n - 1, start + 3 * size * size)

            # Combine quadrants:
            top = [q4[i] + q1[i] for i in range(size)]
            bottom = [q3[i] + q2[i] for i in range(size)]
            return top + bottom

        return build(n, 0)
