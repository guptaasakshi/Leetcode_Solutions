class Solution {
public:
    string reverseParentheses(string s) {
        stack<int> openIdxs;
        string ans = "";
        
        for(int i = 0; i < s.size(); i++){
            switch(s[i]){
                case '(':{
                    openIdxs.push(ans.size());
                    break;
                }case ')':{
                    int openIdx = openIdxs.top(); openIdxs.pop();
                    reverse(ans.begin() + openIdx, ans.end());
                    break;
                }default:{
                    ans += s[i];
                    break;
                }
            }
        }
        
        return ans;
    }
};

