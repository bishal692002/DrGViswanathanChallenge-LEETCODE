class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        original = ""
        reverse = ""

        for char in s:
            if char.isalnum():
                original = original + char
                reverse = char + reverse

        return original == reverse