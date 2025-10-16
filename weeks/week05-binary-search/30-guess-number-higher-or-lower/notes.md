# Notes

## Link
https://leetcode.com/problems/guess-number-higher-or-lower/description/

## Approach
1. Use binary search between `1` and `n`.  
2. Get the middle value `mid` each round and call `guess(mid)`.  
3. If `guess(mid)` returns:  
   - `0`: found the number.  
   - `-1`: target is smaller → move `rear` to `mid`.  
   - `+1`: target is larger → move `front` to `mid`.  
4. Repeat until the correct number is found.

## Code
``` python
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        front, rear = 1, n
        if guess(front) == 0:
            return front
        elif guess(rear) == 0:
            return rear
        else:
            while True:
                mid = (front+rear)//2
                g = guess(mid)
                if g < 0:
                    rear = mid
                elif g > 0:
                    front = mid                    
                else:
                    return mid
                
        return 0
```

## Complexity Analysis
- **Time:** O(log n) — Each call halves the search range.  
- **Space:** O(1) — Only constant variables are used.

## Review
- Classic binary search pattern with clear decision flow.  
- The `guess()` API defines comparison logic, so no direct comparison is needed.
- Efficient and simple approach; terminates in logarithmic time.
- Make sure to handle the loop condition properly to avoid infinite loops.