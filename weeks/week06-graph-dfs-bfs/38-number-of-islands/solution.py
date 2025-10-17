from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        h,w = len(grid), len(grid[0])
        answer = 0
        for y in range(h):
            for x in range(w):
                if grid[y][x] == "1":
                    queue = deque([(x,y)])
                    grid[y][x] = 0
                    answer += 1
                    while queue:
                        cx, cy = queue.popleft()
                        for nx, ny in [(cx+1,cy),(cx,cy+1),(cx-1,cy),(cx,cy-1)]:
                            if (0<=nx<w and 0<=ny<h) and grid[ny][nx] == "1":
                                grid[ny][nx] = "0"
                                queue.append((nx,ny))
        return answer
        