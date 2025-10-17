# Notes

## Link
https://leetcode.com/problems/number-of-islands/

## Approach
- Scan all cells. When you hit `"1"`, that’s a **new island** → `answer += 1`.
- Run **BFS** from that cell:
  - Push it to a queue and flip to `"0"` immediately (this is **visited**).
  - Pop cells, check 4 neighbors; if neighbor is `"1"`, flip to `"0"` and enqueue.
- Continue until the queue is empty; repeat for the whole grid.

## Code
``` python
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
```

## Complexity Analysis
- **Time:** `O(n^2)` — each cell is processed at most once.  
- **Space:** `O(n^2)` — worst case queue size when one island fills the grid.

## Review
- Flipping to `"0"` **on enqueue** prevents duplicate visits.
- BFS or DFS both work; BFS avoids recursion depth limits.
- Pitfall: keep types consistent (`"1"`/`"0"` as strings throughout).
