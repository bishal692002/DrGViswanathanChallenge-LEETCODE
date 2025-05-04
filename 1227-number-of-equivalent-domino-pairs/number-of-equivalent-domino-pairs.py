class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        dict1, count = defaultdict(int), 0

        for i,j in dominoes:
            min_val = min(i,j)
            max_val = max(i,j)
            count += dict1[(min_val,max_val)]
            dict1[(min_val,max_val)] += 1 

        return count
        
        