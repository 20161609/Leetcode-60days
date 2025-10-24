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
