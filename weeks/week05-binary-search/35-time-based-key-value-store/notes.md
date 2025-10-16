# Notes

## Link
https://leetcode.com/problems/time-based-key-value-store/description/

## Approach
1. Use two dictionaries for each key:  
   - `values[key]`: maps timestamp → value.  
   - `stamp[key]`: stores timestamps in ascending order.  
2. When `set()` is called, append the timestamp and record its value.  
3. When `get()` is called:  
   - If the exact timestamp exists, return it.  
   - Otherwise, use `bisect_right()` to find the **largest timestamp smaller than** the given one.  
   - Return the value for that timestamp.

## Code
``` python
from bisect import bisect_right

class TimeMap:

    def __init__(self):
        self.box = {}
        self.values = {}
        self.stamp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.values:
            self.values[key], self.stamp[key] = {}, []
        self.values[key][timestamp] = value
        self.stamp[key].append(timestamp)
        
    def get(self, key: str, timestamp: int) -> str:
        if not key in self.stamp or timestamp < self.stamp[key][0]:
            return ""

        if not timestamp in self.values[key]:
            idx = bisect_right(self.stamp[key], timestamp)
            timestamp = self.stamp[key][min(idx-1, len(self.stamp[key])-1)]
        return self.values[key][timestamp]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
```

## Complexity Analysis
- **Time:** O(log n) for each `get()` due to binary search, O(1) for `set()`.  
- **Space:** O(n) — stores all timestamps and values.

## Review
- This solution uses `bisect_right()` for fast timestamp lookup.  
- **What `bisect_right()` does:**  
  It finds the insertion index where the given number would fit in a **sorted list** while keeping order.  
  So `bisect_right(stamps, t)` gives the position *after* the last timestamp ≤ `t`.  
  We then move one step back (`idx - 1`) to get the right value for `t`.  
- Simple, clean approach for handling time-based lookups without manual binary search.  
- `bisect` module helps write shorter and safer code for sorted sequence problems.
