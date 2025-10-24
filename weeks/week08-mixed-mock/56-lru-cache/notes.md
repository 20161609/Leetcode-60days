# Notes

## Link
https://leetcode.com/problems/lru-cache/

## Approach
Used `OrderedDict` to maintain insertion order and achieve O(1) updates.  
When a key is accessed or inserted, it's moved to the end (most recently used).  
When capacity is exceeded, the least recently used key (at the front) is removed.

## Code
``` python
from collections import deque, OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.box = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if not key in self.box:
            return -1
        self.box.move_to_end(key)        
        return self.box[key]

    def put(self, key: int, value: int) -> None:
        if key in self.box:
            self.box.move_to_end(key)
        self.box[key] = value
        if len(self.box) > self.capacity:
            self.box.popitem(last=False)
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

## Complexity Analysis
- Time: O(1) for both `get` and `put` (thanks to OrderedDict)
- Space: O(n) for capacity

## Review
- `OrderedDict.move_to_end()` lets us reorder keys efficiently.
- Using `popitem(last=False)` removes the least recently used key in O(1).
- Much faster and cleaner than using `deque.remove()` which was O(n).
- Great example of how built-in data structures can simplify LRU logic.
