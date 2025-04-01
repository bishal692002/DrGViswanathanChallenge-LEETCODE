class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
    
        hello = {}
        for r in magazine:
            if r in hello:
                hello[r] += 1
            else:
                hello[r] = 1
        for r in ransomNote:
            if r in hello and hello[r]>0:
                hello[r] -= 1
            else:
                return False
        return True
        