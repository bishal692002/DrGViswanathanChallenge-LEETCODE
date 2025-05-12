class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1 = {}
        t1 = {}
        for has in s:
            if has in s1:
                s1[has] += 1
            else:
                s1[has] = 1
        for has in t:
            if has in t1:
                t1[has] += 1
            else:
                t1[has] = 1
        return s1 == t1
        
        

        