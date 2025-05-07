class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        mp={}
        cp={}
        for i in range(len(s)):
            if s[i] in mp:
                if mp[s[i]]!=t[i]:
                    return False
            else:
                if t[i] in cp:
                    return False
            mp[s[i]]=t[i]
            cp[t[i]]=s[i]
        return True

        
