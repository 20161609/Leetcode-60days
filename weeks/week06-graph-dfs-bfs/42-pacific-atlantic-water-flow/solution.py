from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        h, w = len(heights), len(heights[0])
        paci = [[0] * w for _ in range(h)]
        atla = [[0] * w for _ in range(h)]        
        queue = deque([])
        for x,y in [(x, 0) for x in range(w)] + [(0, y) for y in range(h)]:
            if paci[y][x] == 1:
                continue
            paci[y][x] = 1
            queue.append((x,y))
            while queue:
                x, y= queue.popleft()
                for nx, ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if not (0<=nx<w and 0<=ny<h): 
                        continue
                    if paci[ny][nx] or (heights[ny][nx] < heights[y][x]):
                        continue
                    paci[ny][nx] = 1
                    queue.append((nx,ny))

        for x,y in [(x, h-1) for x in range(w)] + [(w-1, y) for y in range(h)]:
            if atla[y][x] == 1:
                continue
            atla[y][x] = 1
            queue.append((x,y))
            while queue:
                x, y= queue.popleft()
                for nx, ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if not (0<=nx<w and 0<=ny<h): 
                        continue
                    if atla[ny][nx] or (heights[ny][nx] < heights[y][x]):
                        continue
                    atla[ny][nx] = 1
                    queue.append((nx,ny))
        
        answer = []
        for y in range(h):
            for x in range(w):
                if atla[y][x] and paci[y][x]:
                    answer.append([y,x])
        return answer