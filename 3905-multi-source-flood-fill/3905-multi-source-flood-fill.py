from collections import deque, defaultdict

class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        
        grid = [[0]*m for _ in range(n)]
        q = deque()
        
        # Step 1: Initialize sources
        for r, c, color in sources:
            grid[r][c] = color
            q.append((r, c, color))
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # Step 2: BFS
        while q:
            size = len(q)
            temp = {}  # (r,c) -> max color
            
            for _ in range(size):
                r, c, color = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0:
                        if (nr, nc) not in temp:
                            temp[(nr, nc)] = color
                        else:
                            temp[(nr, nc)] = max(temp[(nr, nc)], color)
            
            # Assign colors after full level
            for (r, c), color in temp.items():
                grid[r][c] = color
                q.append((r, c, color))
        
        return grid