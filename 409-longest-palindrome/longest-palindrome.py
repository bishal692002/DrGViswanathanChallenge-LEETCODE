from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        count = Counter(s)
        length = 0
        odd_found = False

        for freq in count.values():
            length += freq // 2 * 2
            if freq % 2 == 1:
                odd_found = True

        if odd_found:
            length += 1

        return length