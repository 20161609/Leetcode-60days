# Notes

## Link
https://leetcode.com/problems/longest-substring-without-repeating-characters/

## Approach
1. Use an pointer index `front` to represent the start index of the latest substring.
2. Use a dict `box` to store the most recent index where each character appeared in the string `s`.
3. Iterate through the string `s` using `rear` and update the dict `box` in each loof.
4. If the duplication of character `c` is found, remove all charaters from `front` to `box[c]`, then move `front` to `box[c]` + 1.
5. After all iteratings, return the max size of valid substing encounterd.

## Code
```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        box = dict()
        front, answer = 0, 0
        for rear, c in enumerate(s):
            if not c in box:
                box[c] = rear
            else: # Duplicated
                for i in range(front, box[c]):
                    box.pop(s[i])
                front = box.pop(c) + 1
                box[c] = rear
            answer = max(answer, len(box))

        return answer
```

## Complexity Analysis
- Time: O(n)
- Space: O(n)

## Review
- Why is that time complexity O(n)?: First of all, iterating all characters in string `s` takes O(n). But how many time complexity to remove characters from the dict `box`? One removal of one character can occur per one index in string `s`. So it also takes O(n). So entire time complexity would be O(n).