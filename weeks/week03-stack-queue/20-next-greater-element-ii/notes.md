# Notes

## Link
https://leetcode.com/problems/next-greater-element-ii/description/

## Approach
1. Use `stack` to store the latest index which didn't find anything greater than itself.
2. In each loop(`for`), compare current num to `stack`'s top. If the `stack`'s top is less than current num, pop the stack. If there's no more, push the current num to the `stack`.

## Code
```
from collections import deque

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [-1] * n
        stack = deque([])        
        for i in range(n*2):
            i %= n
            while stack and nums[stack[-1]] < nums[i]:
                answer[stack.pop()] = nums[i]
            stack.append(i)
        return answer
```

## Complexity Analysis
- Time: O(n)
- Space: O(n)

## Review
1. Why should I use `stack`? -> I need to get the latest one. The `stack`'s top always represents the most recent element waiting for a greater number.
2. Store **indexes**, not values — so you can update `answer` correctly.  
3. Loop `2 * n` times to handle the **circular array**.  
4. Use `i %= n` to wrap around the index.  
5. `-1` means no greater element exists.  
6. Key idea: maintain a **monotonic decreasing stack** and update when a larger number appears.
