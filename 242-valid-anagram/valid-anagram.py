class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        s1 = {}
        t1 = {}

        for num in s:
            s1[num] = s1.get(num,0)+1 
        for num in t:
            t1[num] = t1.get(num,0)+1 
        return s1 == t1