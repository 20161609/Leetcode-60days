# Notes

## Link
https://leetcode.com/problems/minimum-window-substring/

## Approach
1. Use two hash maps:  
   - `goal`: required frequency of each character in `t`.  
   - `box`: current frequency in the sliding window.  
2. Expand the right pointer to include characters.  
3. When all characters in `t` are covered, shrink from the left to find the smallest valid window.  
4. Keep track of the minimum window boundaries and return the substring.

## Code
``` python
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
```

## Complexity Analysis
- Time: `O(n)` — Each index in `s` is visited at most once by both `left` and `right` pointers.  
  This makes the total number of pointer movements linear, not quadratic.  
- Space: `O(k)` — Hash maps store unique characters from `t`.

## Review
- Sliding window keeps balance between expansion and contraction.  
- `goal` defines what we need; `box` tracks what we have.  
- Once all target characters are satisfied, try to shrink the window.  
- The algorithm guarantees the smallest valid window without missing any case.  
- Efficient and clean solution for substring problems involving frequency matching.
