class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        
        #k = 3
        #original - 1 2 3 4 5 6 7 
        #expected- 5 6 7 1 2 3 4
        l,r = 0 ,len(nums)-1
        while l<r:#here- 7 6 5 4 3 2 1 
            nums[l],nums[r] = nums[r],nums[l]
            l,r = l+1,r-1
        
        l,r = 0 ,k-1 
        while l<r:#here 5 6 7, 4 3 2 1
            nums[l],nums[r] = nums[r],nums[l]
            l,r = l+1,r-1

        l,r = k,len(nums)-1 
        while l<r:# 5 6 7, 1 2 3 4
            nums[l],nums[r] = nums[r],nums[l]
            l,r = l+1,r-1
        
        