class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        cnt = Counter()
        count_pairs = ans = 0
        n = len(nums)
        while True:
            while r < n and count_pairs < k:
                count_pairs += cnt[nums[r]]
                cnt[nums[r]] += 1
                r += 1
            if count_pairs < k:
                break
            ans += n - r + 1
            cnt[nums[l]] -= 1
            count_pairs -= cnt[nums[l]]
            l += 1
        return ans