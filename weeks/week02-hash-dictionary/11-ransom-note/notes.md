# Notes

## Link
https://leetcode.com/problems/ransom-note/description/

## Approach
1. Use dict `box` to store which characters are included in string `ransomNote` and how many times each character appears.
2. Iterate through the string `magazine` and if the character matches the dict `box`, the number decreases by 1.(If zero, it should be removed from the dict `box`.)
3. If the box is empty in a loop, return True.
4. Even if the iterating has been complete but there's no loop where the box is empty, return False.

## Code
```
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        box = {}
        for c in ransomNote:
            if not c in box:
                box[c] = 0
            box[c] += 1
        for c in magazine:
            if c in box:
                box[c] -= 1
                if box[c] == 0:
                    box.pop(c)
                    if len(box) == 0:
                        return True
        
        return False
```

## Complexity Analysis
- Time: O(n)
- Space: O(n)

## Review
- How to compare 2 strings?: Use dict `box` to store how many times each charater appears and which character appears. And in the sliding, each window can be checked if it matches `box`.