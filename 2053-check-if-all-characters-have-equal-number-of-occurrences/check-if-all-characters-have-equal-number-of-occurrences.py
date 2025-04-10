class Solution(object):
    def areOccurrencesEqual(self, s):
        counts = {}
        for num in s:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        return  len(set(counts.values())) == 1
            

        