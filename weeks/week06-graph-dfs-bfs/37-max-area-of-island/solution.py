from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        answer = 0
        for y in range(h):
            for x in range(w):
                if grid[y][x] == 1:
                    queue = deque([(x,y)])
                    grid[y][x] = 0
                    area = 0
                    while queue:
                        px, py = queue.popleft()
                        area += 1
                        for nx,ny in [(px+1,py),(px-1,py),(px,py+1),(px,py-1)]:
                            if (0<=nx<w and 0<=ny<h) and grid[ny][nx] == 1:
                                queue.append((nx, ny))
                                grid[ny][nx] = 0
                    answer = max(answer, area)

        return answer