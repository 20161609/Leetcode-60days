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