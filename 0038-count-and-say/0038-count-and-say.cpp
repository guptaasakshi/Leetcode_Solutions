class Solution {
public:
    string countAndSay(int n) {
        string result = "1";
        
        for (int i = 2; i <= n; i++) {
            string temp = "";
            
            for (int j = 0; j < result.size(); j++) {
                int count = 1;
                
                // count same digits
                while (j + 1 < result.size() && result[j] == result[j + 1]) {
                    count++;
                    j++;
                }
                
                temp += to_string(count) + result[j];
            }
            
            result = temp;
        }
        
        return result;
    }
};