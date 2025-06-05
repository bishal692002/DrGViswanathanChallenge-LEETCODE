class Solution(object):
    def firstPalindrome(self, words):
        def check(word):
            i=0
            j=len(word)-1
            while i<j:
                if word[i]!=word[j]:
                    return False
                i+=1
                j-=1
            return True
    
        for word in words:
            if check(word)==True:
                return word
            continue
        return ("")      