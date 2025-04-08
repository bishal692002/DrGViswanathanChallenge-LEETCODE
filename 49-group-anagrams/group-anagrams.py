class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
        for word in strs:
            sorte = "".join(sorted(word))
            if sorte in anagrams:
                anagrams[sorte].append(word)
            else:
                anagrams[sorte] = [word]
        return list(anagrams.values())

        