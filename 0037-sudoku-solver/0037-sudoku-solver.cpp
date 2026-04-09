class Solution {
public:

    bool isValid(vector<vector<char>>& board, int row, int col, char num) {
        for (int i = 0; i < 9; i++) {
            // row check
            if (board[row][i] == num) return false;

            // col check
            if (board[i][col] == num) return false;

            // box check
            int r = 3 * (row / 3) + i / 3;
            int c = 3 * (col / 3) + i % 3;
            if (board[r][c] == num) return false;
        }
        return true;
    }

    bool solve(vector<vector<char>>& board) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {

                if (board[i][j] == '.') {

                    for (char num = '1'; num <= '9'; num++) {

                        if (isValid(board, i, j, num)) {
                            board[i][j] = num;

                            if (solve(board))
                                return true;

                            // backtrack
                            board[i][j] = '.';
                        }
                    }

                    return false; // no valid number
                }
            }
        }
        return true; // solved
    }

    void solveSudoku(vector<vector<char>>& board) {
        solve(board);
    }
};