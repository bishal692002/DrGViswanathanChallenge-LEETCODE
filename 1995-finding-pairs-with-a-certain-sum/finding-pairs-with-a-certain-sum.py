class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
class FindSumPairs:

    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
        self.counts = Counter(nums2)

    def add(self, index, val):
        cur_val = self.nums2[index]
        self.counts[cur_val] -= 1
        self.counts[cur_val + val] = self.counts.get(cur_val + val, 0) + 1
        self.nums2[index] = cur_val + val

    def count(self, tot):
        return sum(self.counts[tot - num] for num in self.nums1)


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)