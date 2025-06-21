class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        hmap = {}

        for ar in arr:
            hmap[ar] = hmap.get(ar,0)+1
        
        
        return len(hmap.values()) == len(set(hmap.values()))