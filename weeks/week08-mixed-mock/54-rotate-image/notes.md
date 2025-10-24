# Notes

## Link
https://leetcode.com/problems/rotate-image/description/

## Approach
1. Rotate the matrix **layer by layer** (from outer ring to inner ring).
2. For each layer `i`, traverse the ring in order and use a `deque` as a buffer:
   - Push the top edge, then right edge, then bottom edge, then left edge values into the queue.
   - While traversing edges again, **pop** from the queue to write rotated values into their new positions.
3. This effectively performs a 90° clockwise rotation of the ring. Repeat for all `n//2` layers.

## Code
``` python
from collections import deque

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        queue = deque()
        for i in range(n//2):
            y = i
            for x in range(i, n-i-1):
                queue.append(matrix[y][x])
            
            x = n - i - 1
            for y in range(i, n-i-1):
                queue.append(matrix[y][x])
                matrix[y][x] = queue.popleft()
            
            y = n - i - 1
            for x in range(i+1, n-i)[::-1]:
                queue.append(matrix[y][x])
                matrix[y][x] = queue.popleft()

            x = i
            for y in range(i+1, n-i)[::-1]:
                queue.append(matrix[y][x])
                matrix[y][x] = queue.popleft()

            y = i
            for x in range(i, n-i-1):
                matrix[y][x] = queue.popleft()

        return None
```

## Complexity Analysis
- **Time:** O(n^2) — Each element is moved once.
- **Space:** O(n) — Extra queue for a ring (worst ring length is O(n)).

## Review
- Layered ring rotation keeps the operation in-place (matrix updated directly) while the queue preserves order during the cycle.
- Be careful with **bounds and order** on each edge to avoid off-by-one errors and double writes.
- Clear the queue correctly per layer; push/pop sequences must align with edge traversal.
- Alternatives:
  - **Transpose + reverse each row** (most common): O(n^2) time, O(1) extra space.
  - **Four-way swap** per cell in a layer, also O(1) extra space.