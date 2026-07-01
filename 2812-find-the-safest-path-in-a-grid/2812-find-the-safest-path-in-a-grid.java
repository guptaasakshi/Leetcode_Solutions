import java.util.*;

class Solution {
    public int maximumSafenessFactor(List<List<Integer>> grid) {
        int n = grid.size();

        int[][] dist = new int[n][n];
        for (int[] row : dist) {
            Arrays.fill(row, -1);
        }

        Queue<int[]> queue = new LinkedList<>();

        // Step 1: Put all thieves in queue
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid.get(i).get(j) == 1) {
                    queue.offer(new int[]{i, j});
                    dist[i][j] = 0;
                }
            }
        }

        int[][] dirs = {
            {1, 0},
            {-1, 0},
            {0, 1},
            {0, -1}
        };

        // Multi-source BFS
        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int row = cell[0];
            int col = cell[1];

            for (int[] dir : dirs) {
                int newRow = row + dir[0];
                int newCol = col + dir[1];

                if (newRow >= 0 && newRow < n &&
                    newCol >= 0 && newCol < n &&
                    dist[newRow][newCol] == -1) {

                    dist[newRow][newCol] = dist[row][col] + 1;
                    queue.offer(new int[]{newRow, newCol});
                }
            }
        }

        // Step 2: Max heap to find safest path
        PriorityQueue<int[]> pq = new PriorityQueue<>(
            (a, b) -> b[2] - a[2]
        );

        boolean[][] visited = new boolean[n][n];

        pq.offer(new int[]{0, 0, dist[0][0]});

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();

            int row = curr[0];
            int col = curr[1];
            int safe = curr[2];

            if (visited[row][col]) {
                continue;
            }

            visited[row][col] = true;

            if (row == n - 1 && col == n - 1) {
                return safe;
            }

            for (int[] dir : dirs) {
                int newRow = row + dir[0];
                int newCol = col + dir[1];

                if (newRow >= 0 && newRow < n &&
                    newCol >= 0 && newCol < n &&
                    !visited[newRow][newCol]) {

                    int newSafe = Math.min(safe, dist[newRow][newCol]);

                    pq.offer(new int[]{newRow, newCol, newSafe});
                }
            }
        }

        return 0;
    }
}