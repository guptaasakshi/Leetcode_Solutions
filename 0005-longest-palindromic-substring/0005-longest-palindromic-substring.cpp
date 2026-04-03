class Solution {
public:
    string longestPalindrome(string s) {
        int start = 0, maxLen = 0;

        for (int i = 0; i < s.length(); i++) {
            expand(s, i, i, start, maxLen);     // odd
            expand(s, i, i + 1, start, maxLen); // even
        }

        return s.substr(start, maxLen);
    }

    void expand(string &s, int left, int right, int &start, int &maxLen) {
        while (left >= 0 && right < s.length() && s[left] == s[right]) {
            int len = right - left + 1;

            if (len > maxLen) {
                start = left;
                maxLen = len;
            }

            left--;
            right++;
        }
    }
};