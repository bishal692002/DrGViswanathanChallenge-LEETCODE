class Solution:
    def longestPalindrome(self, s):
        if len(s) <= 1:
            return s
        
        maxlen = 1
        maxstr = s[0]
        
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                substring = s[i:j+1]
                if len(substring) > maxlen and substring == substring[::-1]:
                    maxlen = len(substring)
                    maxstr = substring
        
        return maxstr