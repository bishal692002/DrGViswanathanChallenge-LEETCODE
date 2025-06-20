class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hmap={}
        maxval=0
        res=0
        for num in nums:
            hmap[num]=hmap.get(num,0)+1
            if hmap[num]>maxval:
                maxval=hmap[num]

        
        for k in hmap.keys():
            if hmap[k]==maxval:
                res+=hmap[k]
        return res