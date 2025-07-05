class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        maxi = []
        hmap = {}
        for char in arr:
            hmap[char] = hmap.get(char, 0) + 1

        for key, value in hmap.items():
            if value == key:
                maxi.append(value)

        if maxi:
            return max(maxi)
        return -1
