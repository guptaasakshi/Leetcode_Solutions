class Solution {
public:
    vector<int> sequentialDigits(int low, int high) {
        // Queue to store candidate sequential digits
        queue<int> q;

        // Initialize the queue with single-digit integers from 1 to 8
        for(int i = 1; i<= 8; i++) {
            q.push(i);
        }

        // Vector to store the final result
        vector<int> result;
        
        // Process elements in the queue
        while(!q.empty()) {
            // Get the front element of the queue
            int temp = q.front();
            q.pop();

            // Check if the element is within the specified range [low, high]
            if(temp >= low && temp <= high) {
                result.push_back(temp);
            }

            // Calculate the last digit of the current element
            int last_digit = temp % 10;

            // If the next digit is within the range [1, 9], add it to the queue
            if(last_digit + 1 <= 9) {
                q.push(temp * 10 + (last_digit + 1));
            }
        }
        // Return the final result
        return result;
    }
};