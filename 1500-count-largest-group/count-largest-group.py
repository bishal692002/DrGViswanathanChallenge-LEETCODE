class Solution(object):
    def countLargestGroup(self, n):
        count = {}
        for i in xrange(1, n + 1):
            digit_sum = sum(int(d) for d in str(i))
            if digit_sum in count:
                count[digit_sum] += 1
            else:
                count[digit_sum] = 1

        max_size = max(count.values())
        result = 0
        for group_size in count.values():
            if group_size == max_size:
                result += 1

        return result
