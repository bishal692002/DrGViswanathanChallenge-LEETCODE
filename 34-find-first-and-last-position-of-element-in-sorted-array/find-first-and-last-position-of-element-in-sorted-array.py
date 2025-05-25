class Solution(object):
    def searchRange(self, nums, target):
        st=[]
        for i in range(len(nums)):
            if nums[i]==target:
                st.append(i)
        if len(st)>0:
            return [st[0],st[-1]]
        else:
            return [-1,-1]
                