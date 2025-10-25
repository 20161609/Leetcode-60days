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