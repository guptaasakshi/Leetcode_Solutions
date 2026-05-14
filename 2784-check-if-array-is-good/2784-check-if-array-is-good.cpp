class Solution {
public:
    bool isGood(vector<int>& nums) {
        int n = nums.size() - 1;
        int max = 0;
        int min = 101;
        int n_count = 0;

        for (const auto &elem : nums) {
            if (elem > n || elem < 1) {
                return false;
            }

            if (elem == max || elem == min) {
                return false;
            }

            if (elem == n) {
                n_count++;
                continue;
            } 
            
            if (elem > max) {
                max = elem;
            } 

            if (elem < min) {
                min = elem;
            }
        }

        if (n_count == 2) {
            return true;
        }
        
        return false;
    }
};