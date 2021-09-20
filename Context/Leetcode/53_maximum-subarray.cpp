# [maximum_average_segment](https://e-maxx.ru/algo/maximum_average_segment)

class Solution {
private:
    
public:
    int maxSubArray(vector<int>& nums) {
        int ans = nums[0], 
        int sum = 0, 
        int min_sum = 0;

        for(int i = 0; i < nums.size(); i++){
            sum += nums[i];
            ans = max(ans, sum - min_sum);
            min_sum = min(min_sum, sum);
        }
        return ans;
    }
    
};