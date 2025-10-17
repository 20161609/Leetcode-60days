# Notes

## Link
https://leetcode.com/problems/flood-fill/

## Approach
- Start color = `image[sr][sc]`.  
- **BFS** with a queue from `(sr, sc)`; explore 4 directions.  
- Only push neighbors that are **in-bounds**, **unvisited**, and **equal to the start color**.  
- Mark as visited **when you enqueue**; paint the pixel when you pop from the queue.  
- (Micro-opt) If `color == start color`, you can return early.

## Code
``` python
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        queue = deque([(sc, sr)])
        H, W = len(image), len(image[0])

        visited = set([(sc,sr)])
        while queue:
            x,y = queue.popleft()
            image[y][x] = color
            for nx, ny in [(x+1, y), (x, y+1), (x-1,y), (x,y-1)]:
                if (0<=nx<W and 0<=ny<H) and (not (nx,ny) in visited):
                    if image[ny][nx] == original:
                        queue.append((nx, ny))
                        visited.add((nx,ny))

        return image
```

## Complexity Analysis
- **Time:** `O(n^2)` — each cell is processed at most once.  
- **Space:** `O(n^2)` — worst case for `visited` + queue.

## Review
- BFS or DFS both work; BFS avoids recursion depth issues.  
- Marking visited on **enqueue** prevents duplicate work.  
- Painting on pop keeps the “should we visit?” check simple (compare to original color).  
- Common pitfalls: forgetting bounds checks, not guarding revisits, or missing the early exit when target color equals the start color.
