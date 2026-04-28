import java.util.*;

class Solution {
    public int minOperations(int[][] grid, int x) {
        List<Integer> list = new ArrayList<>();
        
        int rem = grid[0][0] % x;
        
        // Step 1 & 2: flatten + check feasibility
        for (int[] row : grid) {
            for (int num : row) {
                if (num % x != rem) {
                    return -1;
                }
                list.add(num);
            }
        }
        
        // Step 3: sort
        Collections.sort(list);
        
        // Step 4: median
        int median = list.get(list.size() / 2);
        
        // Step 5: calculate operations
        int ops = 0;
        for (int num : list) {
            ops += Math.abs(num - median) / x;
        }
        
        return ops;
    }
}