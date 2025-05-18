class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort()
        result=[intervals[0]]
        
        for i in intervals:
            if i[0]<=result[-1][1]:
                result[-1][1]= max(result[-1][1],i[1])
            else:
                result.append(i)
        return result
        