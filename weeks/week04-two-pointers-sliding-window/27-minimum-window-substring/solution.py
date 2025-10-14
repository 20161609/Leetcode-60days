class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        goal, box = {}, {}
        for x in t:
            if not x in goal:
                goal[x], box[x] = 0, 0
            goal[x] += 1
        
        score = 0
        front, rear = -1, len(s)
        left = 0
        for right in range(len(s)):
            if s[right] in box:
                box[s[right]] += 1
                score += int(box[s[right]] <= goal[s[right]])
                while score == len(t):
                    if rear - front > right - left:
                        rear, front = right, left
                    if left == right:
                        break
                    if s[left] in box:
                        box[s[left]] -= 1
                        score -= int(box[s[left]] < goal[s[left]])
                    left += 1

        if front == -1:
            rear = front
        return s[front:rear+1:]