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
            s1[has] = s1.get(has,0)+1
            
        for has in t:
            t1[has] = t1.get(has,0)+1
        return s1 == t1
        
        

        