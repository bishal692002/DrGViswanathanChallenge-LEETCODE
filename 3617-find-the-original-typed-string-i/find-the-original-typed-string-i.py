class Solution(object):
    def possibleStringCount(self, word):
        curr = word[0]
        count = 0
        for a in word:
            if a == curr:
                count += 1
            else:
                curr = a
        return count