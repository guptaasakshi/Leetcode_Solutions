class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> res;

        // Step 1: sort
        sort(intervals.begin(), intervals.end());

        for (auto& interval : intervals) {
            // agar empty hai ya overlap nahi hai
            if (res.empty() || res.back()[1] < interval[0]) {
                res.push_back(interval);
            } 
            else {
                // merge
                res.back()[1] = max(res.back()[1], interval[1]);
            }
        }

        return res;
    }
};