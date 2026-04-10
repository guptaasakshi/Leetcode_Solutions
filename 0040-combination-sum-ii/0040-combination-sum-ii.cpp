class Solution {
public:
    void backtrack(int start, vector<int>& candidates, int target,
                   vector<int>& temp, vector<vector<int>>& ans) {
        
        if (target == 0) {
            ans.push_back(temp);
            return;
        }
        
        for (int i = start; i < candidates.size(); i++) {
            
            // 🔥 skip duplicates
            if (i > start && candidates[i] == candidates[i - 1]) continue;
            
            // optimization
            if (candidates[i] > target) break;
            
            temp.push_back(candidates[i]);
            
            // 🔥 i+1 (reuse NOT allowed)
            backtrack(i + 1, candidates, target - candidates[i], temp, ans);
            
            temp.pop_back();
        }
    }
    
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> ans;
        vector<int> temp;
        
        sort(candidates.begin(), candidates.end()); // 🔥 must
        
        backtrack(0, candidates, target, temp, ans);
        
        return ans;
    }
};