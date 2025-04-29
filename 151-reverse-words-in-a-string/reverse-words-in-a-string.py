class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = s.split()
        result.reverse()
        return " ".join(result)
        