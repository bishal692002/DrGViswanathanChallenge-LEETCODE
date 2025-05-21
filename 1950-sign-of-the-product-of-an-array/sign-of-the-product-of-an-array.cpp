class Solution {
public:
    int arraySign(vector<int>& nums) {
        double prod = 1, i;
        for (i = 0; i < nums.size(); i++) {
            prod = prod * nums[i];
        }
        if (prod < 0) {
            return -1;
        } else if (prod > 0) {
            return 1;
        } else {
            return 0;
        }
    }
};