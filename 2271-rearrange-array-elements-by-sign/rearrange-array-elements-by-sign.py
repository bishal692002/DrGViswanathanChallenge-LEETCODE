class Solution(object):
    def rearrangeArray(self, nums):
        n = len(nums)
        
        pos = [0] * (n // 2)
        neg = [0] * (n // 2)
        
        p = 0
        q = 0
        
        # Separate positives and negatives
        for num in nums:
            if num < 0:
                neg[q] = num
                q += 1
            else:
                pos[p] = num
                p += 1
        
        # Build result
        res = [0] * n
        idx = 0
        for i in range(p):
            res[idx] = pos[i]
            res[idx + 1] = neg[i]
            idx += 2
        
        return res
