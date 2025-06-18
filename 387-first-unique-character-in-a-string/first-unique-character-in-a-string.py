class Solution(object):
    def firstUniqChar(self, s):
        hmap = {}
        for char in s:
            if char in hmap:
                hmap[char] += 1
            else:
                hmap[char] = 1

        for i in range(len(s)):
            char = s[i]
            if hmap[char] == 1:
                return i
        
        return -1