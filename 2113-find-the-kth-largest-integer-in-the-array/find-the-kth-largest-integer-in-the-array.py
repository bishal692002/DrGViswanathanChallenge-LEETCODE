class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        n = []
        for i in nums:
            i = int(i)
            n.append(i)

        n.sort(reverse=True)
        nth = str(n[k-1])

        return nth

        

        

        