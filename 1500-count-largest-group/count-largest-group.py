class Solution(object):
    def countLargestGroup(self, n):
        count = {}  

        for i in range(1, n + 1):  
            s = sum(int(d) for d in str(i))
            count[s] = count.get(s, 0) + 1

        max_size = max(count.values())
        return sum(1 for v in count.values() if v == max_size)
