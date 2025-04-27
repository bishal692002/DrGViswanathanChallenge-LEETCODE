class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for tt in t:
            if s.count(tt) < t.count(tt):
                return tt

        