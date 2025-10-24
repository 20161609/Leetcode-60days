# Notes

## Link
https://leetcode.com/problems/lru-cache/

## Approach
Used `OrderedDict` to maintain insertion order and achieve O(1) updates.  
When a key is accessed or inserted, it's moved to the end (most recently used).  
When capacity is exceeded, the least recently used key (at the front) is removed.

## Code
Final implementation is in `solution.py`.

## Complexity Analysis
- Time: O(1) for both `get` and `put` (thanks to OrderedDict)
- Space: O(n) for capacity

## Review
- `OrderedDict.move_to_end()` lets us reorder keys efficiently.
- Using `popitem(last=False)` removes the least recently used key in O(1).
- Much faster and cleaner than using `deque.remove()` which was O(n).
- Great example of how built-in data structures can simplify LRU logic.
