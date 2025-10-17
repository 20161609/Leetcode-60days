# Notes

## Link
https://leetcode.com/problems/max-area-of-island/

## Approach
- Scan every cell. When you see land (`1`), start **BFS** from it.
- Use a queue; push the cell, set it to `0` immediately (acts as **visited**).
- Pop cells, grow `area += 1`, and check 4 neighbors.
- If a neighbor is in-bounds and `1`, push it and flip to `0`.
- Track `answer = max(answer, area)` after each island finishes.

## Code
``` python
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
```

## Complexity Analysis
- **Time:** `O(n^2)` — each cell is visited at most once.
- **Space:** `O(n^2)` in the worst case for the queue (one big island).  
  *(No extra `visited` set; we mutate the grid instead.)*

## Review
- Flipping `1 -> 0` on **enqueue** prevents revisits and keeps logic simple.
- BFS and DFS are both fine; BFS avoids recursion depth issues.
- Common pitfalls: forgetting bounds checks, not marking visited early, or reusing the same `area` across islands.
