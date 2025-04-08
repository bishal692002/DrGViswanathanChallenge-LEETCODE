class Solution {
    public int removeDuplicates(int[] nums) {
        int count = 1;
        int a = nums[0];
        
        for(int i = 1; i < nums.length; i++){
            if(nums[i] != a){
                nums[count] = nums[i];
                count++;
                a = nums[i];
            }
        }
        return count;
        
    }
}
        
    