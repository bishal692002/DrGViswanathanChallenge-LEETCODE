class Solution {
    public int removeDuplicates(int[] nums) {
        ArrayList<Integer> al = new ArrayList<>();
        al.add(nums[0]);
        int a = nums[0];
        
        for(int i = 1; i < nums.length; i++){
            if(nums[i] != a){
                al.add(nums[i]);
                a = nums[i];
            }
        }
        for(int i = 0; i < al.size(); i++){
            nums[i] = al.get(i);
        }
        return al.size();
    }
}
        
    
