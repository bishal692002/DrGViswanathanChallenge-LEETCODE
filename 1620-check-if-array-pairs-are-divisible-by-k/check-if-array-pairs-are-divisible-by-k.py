class Solution:
    def canArrange(self, arr, k):
        if len(arr) % 2 != 0:
            return False

        rem = {}

        
        for num in arr:
            r = num % k
            if r in rem:
                rem[r] += 1
            else:
                rem[r] = 1

       
        for r in rem:
            if r == 0 or r * 2 == k:
                if rem[r] % 2 != 0:
                    return False
            else:
                if (k - r) not in rem or rem[k - r] != rem[r]:
                    return False

        return True