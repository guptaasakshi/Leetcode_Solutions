class Solution:
    def rotateGrid(self, grid, k):
        m = len(grid)
        n = len(grid[0])
        result = [[0] * n for _ in range(m)]
        for i in range(min(m // 2, n // 2)):
            circle = []
            # Left column
            circle += [(j, i) for j in range(i, m-i)]
            # Bottom row
            circle += [(m-1-i, j) for j in range(i+1, n-i)]
            # Right column
            circle += [(j, n-1-i) for j in range(m-2-i, i-1, -1)]
            # Top row
            circle += [(i, j) for j in range(n-2-i, i, -1)]
            for index, (x, y) in enumerate(circle):
                target_x, target_y = circle[(index+k) % len(circle)]
                result[target_x][target_y] = grid[x][y]
        return result