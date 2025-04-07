class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = []
        for index in range(n):
            if index == 0:
                steps.append(1)
            elif index == 1:
                steps.append(2)
            else:
                steps.append(steps[index - 1] + steps[index - 2])
        return steps[-1]