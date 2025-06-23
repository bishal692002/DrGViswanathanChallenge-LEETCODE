class Solution(object):
    def wordPattern(self, s, t):

        t=t.split(" ")
        if len(s)!=len(t):
            return False
        e=set()
        for x in range(len(s)):
            e.add((s[x],t[x]))
        return len(e)==len(set(s))==len(set(t))
        