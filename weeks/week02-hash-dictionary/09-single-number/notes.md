# Notes

## Link
https://leetcode.com/problems/single-number/


## Approach
- All elements in nums should be calculated with XOR(`^`). The result is going to be the answer.

## Code
```
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for n in nums:
            answer ^= n

        return answer
```

## Complexity Analysis
- Time: O(n)
- Space: O(1)

## Review
- The condition is notifying "You must implement a solution with a linear runtime complexity and use only constant extra space.". The is the core challange.
- Use XOR: Let nums [4,1,2,1,2]. And can it be possible to get answer with 4^1^2^1^2?. XOR operator is commutative. So 4^1^2^1^2=4^(2^2)^(1^1)=4^0^0=4.