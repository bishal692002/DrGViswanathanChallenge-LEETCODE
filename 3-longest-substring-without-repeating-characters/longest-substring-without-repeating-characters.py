class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longest=0
        current=""
        for char in s:
            if char in current:
                index=current.index(char)
                current=current[index+1:]
            current+=char
            longest=max(longest,len(current))
        return longest

        
        
        