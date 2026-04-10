class Solution {
public:
    void solve(int idx, vector<int>& candidates, int target, 
               vector<int>& temp, vector<vector<int>>& ans) {
        
        // Base case
        if (target == 0) {
            ans.push_back(temp);
            return;
        }
        
        if (idx == candidates.size() || target < 0) {
            return;
        }
        
        // Include current element
        temp.push_back(candidates[idx]);
        solve(idx, candidates, target - candidates[idx], temp, ans);
        temp.pop_back();
        
        // Skip current element
        solve(idx + 1, candidates, target, temp, ans);
    }
    
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> ans;
        vector<int> temp;
        
        solve(0, candidates, target, temp, ans);
        
        return ans;
    }
};