class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        hmap = {}
        for p in nums:
            hmap[p] = hmap.get(p, 0) + 1
        
        for num in hmap:
            val = hmap[num]
            for i in range(val):
                count += i
        return count


        