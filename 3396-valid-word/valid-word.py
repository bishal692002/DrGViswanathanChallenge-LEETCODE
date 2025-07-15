class Solution(object):
    def isValid(self, word):
        if len(word)<3:
            return False
        hello = {'a','e','i','o','u','A','E','I','O','U'}
        vowel, consonant = False, False

        for char in word:
            if char in hello:
                vowel = True
            elif char.isalpha():  
                consonant = True
            elif char.isdigit():  
                continue
            else:
                return False
        return vowel and consonant
