# Notes

## Link
https://leetcode.com/problems/n-queens/description/

## Approach
1. Backtracking: place one queen at a time and prune invalid positions immediately.
2. Use sets to track conflicts:
   - columns: x_set
   - rows: y_set
   - main diagonals: cross1 uses (x - y)
   - anti diagonals: cross2 uses (x + y)
3. When depth == n, serialize the board and append to answer.
4. visited bitmask is used to avoid revisiting the same occupied-cell set during search.

## Code
``` python
from collections import deque, defaultdict

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        maps = [['.'] * n for _ in range(n)]
        x_set, y_set, cross1, cross2 = set(), set(), set(), set()
        answer, visited = [], set()

        def dfs(x, y, depth, block):
            maps[y][x] = 'Q'
            if depth == n:
                answer.append([''.join(m) for m in maps])
                maps[y][x] = '.'
                return
            
            x_set.add(x), y_set.add(y), cross1.add(x-y), cross2.add(x+y)
            for ny in range(n):
                for nx in range(n):
                    if (nx in x_set) or (ny in y_set): 
                        continue
                    if (nx-ny in cross1) or (nx+ny in cross2):
                        continue
                    if block + 2**(nx+ny*n) in visited:
                        continue
                    visited.add(block + 2**(nx+ny*n))
                    dfs(nx, ny, depth+1, block + 2**(nx+ny*n))

            x_set.remove(x), y_set.remove(y), cross1.remove(x-y), cross2.remove(x+y)
            maps[y][x] = '.'
            return

        for y in range(n):
            for x in range(n):
                x_set.clear(), y_set.clear(), cross1.clear(), cross2.clear()
                visited.add(2**(x+y*n))
                dfs(x,y,1, 2**(x+y*n))

        return answer
```

## Complexity Analysis
- Time: O(n!) in the worst case; pruning cuts a large portion, but the search is still exponential.
- Space: O(n^2) for the board plus O(n) for sets and recursion stack. Output storage adds O(k·n) for k solutions.

## Review
- Core constraints are captured cleanly with x_set, y_set, cross1 (x - y), cross2 (x + y).
- Generating a solution when depth reaches n is straightforward and easy to read.
- You can simplify and speed up:
  - Place queens row by row (or column by column) to remove y_set entirely and avoid scanning the full grid each step.
  - Drop visited bitmask; with row-by-row backtracking, the state is defined by (row, x_set, cross1, cross2).
  - Iterate only valid columns at the current row; this reduces branching and improves clarity.
- Typical minimal skeleton: