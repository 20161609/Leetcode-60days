# Notes

## Link
https://leetcode.com/problems/first-unique-character-in-a-string/description/

## Approach
1. Use dict `box` to store the first index of each character that has appeared exactly once.
2. Use set `abandon` to store all elements abandoned. The character that appears more than once doesn't need to be considered.
3. Iterating through the string `s`, return the minimum index in `box`.
(But, the box is empty and then, it must return -1.)


## Code
```
class Solution:
    def firstUniqChar(self, s: str) -> int:
        box = {}
        abandon = set()
        for i, c in enumerate(s):
            if c in abandon:
                continue
            if not c in box:
                box[c] = i
            else:
                abandon.add(s[box.pop(c)])

        if len(box) == 0:
            return -1
        else:
            return min(box.values())
```

## Complexity Analysis
- Time: O(n)
- Space: O(n)

## Review
- By combining a dict to store unique characters and a set to track duplicates, I can efficiently find the first unique character in a single pass.