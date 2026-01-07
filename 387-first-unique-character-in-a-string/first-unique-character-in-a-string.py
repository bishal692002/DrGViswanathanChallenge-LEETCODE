class Solution(object):
    def firstUniqChar(self, s):
        hmap = {}
        for char in s:
            hmap[char] = hmap.get(char,0) + 1

        for i in range(len(s)):
            if hmap[s[i]] == 1:
                return i
        
        return -1