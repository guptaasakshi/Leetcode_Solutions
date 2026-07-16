class Solution {
public:
    long long gcdSum(vector<int>& nums) {
        int n = nums.size();
        vector<int> mxs(n, 0);
        mxs[0] = nums[0];
        for (int i = 1; i < n; i++) mxs[i] = max(nums[i], mxs[i - 1]);

        vector<int> prefixGcd(n, 0);
        for (int i = 0; i < n; i++) prefixGcd[i] = gcd(nums[i], mxs[i]);

        sort(prefixGcd.begin(), prefixGcd.end());
        long long ans = 0;
        for (int i = 0, j = n - 1; i < j; i++, j--) {
            ans += gcd(prefixGcd[i], prefixGcd[j]);
        }
        return ans;
    }
};