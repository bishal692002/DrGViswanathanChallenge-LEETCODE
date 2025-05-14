class Solution(object):
    def moveZeroes(self, nums):
        i,j=0,0
        while(j<len(nums)):
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            j+=1
        return nums
                    