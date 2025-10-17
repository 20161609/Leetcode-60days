# Notes

## Link
https://leetcode.com/problems/clone-graph/

## Approach
- Use **BFS** with a queue.
- Maintain a map `box` from **original node value → cloned node**.
- When visiting a node, ensure each neighbor has a clone; if not, create it and enqueue the neighbor.
- Append cloned neighbors to the current cloned node’s `neighbors` list.

## Code
``` python
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None

        box = {node.val: Node(node.val)}
        queue = deque([(node)])
        top_val = node.val
        while queue:
            node = queue.popleft()
            if not node:
                continue

            for nxt in node.neighbors:
                if not nxt.val in box:
                    box[nxt.val] = Node(nxt.val)
                    queue.append(nxt)

                box[node.val].neighbors.append(box[nxt.val])

        return box[top_val]

```

## Complexity Analysis
- **Time:** `O(n)`  
- **Space:** `O(n)`  
*(Here `n` counts total nodes and edges processed.)*

## Review
- BFS or DFS both work; BFS avoids recursion depth issues.
- Marking/creating a clone **when first seen** prevents duplicates and handles cycles.
- Caveat: this version keys the map by `val`; if `val` is not unique, key by the **node object** instead.
- Minor cleanups: the `if not node:` inside the loop isn’t needed if you never enqueue `None`.
