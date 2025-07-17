class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        hello = set(candyType)

        return min(len(hello),len(candyType)//2)
        