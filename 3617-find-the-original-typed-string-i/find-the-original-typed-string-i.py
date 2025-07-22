class Solution(object):
    def possibleStringCount(self, word):
        length, ans = len(word), 1
        for i in range(1, length):
            if(len(word) == 1):
                return 1
            elif(word[i] == word[i-1]):
                ans +=1
        return ans