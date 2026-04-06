class Solution {
public:
    vector<string> result;

    void backtrack(string digits, int index, string current, vector<string>& map) {
        // base case
        if (index == digits.size()) {
            result.push_back(current);
            return;
        }

        string letters = map[digits[index] - '0'];

        for (char ch : letters) {
            backtrack(digits, index + 1, current + ch, map);
        }
    }

    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};

        vector<string> map = {
            "", "", "abc", "def", "ghi", "jkl",
            "mno", "pqrs", "tuv", "wxyz"
        };

        backtrack(digits, 0, "", map);
        return result;
    }
};