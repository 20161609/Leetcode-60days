# Notes

## Link
https://leetcode.com/problems/course-schedule/

## Approach
- Build a directed graph with edges `b → a` for each `[a, b]`.
- Collect **roots** (in-degree 0). If there is **no** root, a cycle must exist → return `False`.
- Run **DFS with cycle detection**:
  - `visited`: nodes in the current recursion stack (gray).
  - `checked`: nodes fully processed and proven acyclic (black).
  - If we enter a node already in `visited` → cycle (`False`).
  - If it’s in `checked` → already safe (`True`).
  - After exploring all neighbors, remove from `visited` and add to `checked`.

- Start DFS from every root; finally, return `len(checked) == numCourses`.

## Code
``` python
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        roots = set(range(numCourses))
        for a, b in prerequisites:
            graph[b].append(a)
            if a in roots:
                roots.remove(a)
        if not roots:
            return False

        visited, checked = set(), set()        
        def dfs(node):
            if node in visited:
                return False
            if node in checked:
                return True

            visited.add(node)
            for nxt in graph[node]:
                if not dfs(nxt):
                    return False
            visited.remove(node), checked.add(node)
            return True

        for node in roots:
            if not dfs(node):
                return False
                
        return len(checked) == numCourses
```

## Complexity Analysis
Let `**`n` be `numCourses + len(prerequisites)`.
- Time: `O(n)` — each node and edge is explored at most once.
- Space: `O(n)` — adjacency list, recursion stack, and sets.

## Review
- **Why "no roots ⇒ cycle"?** Every DAG has at least one in-degree-0 node. If none exists, the graph cannot be a DAG → there is a cycle.
- **Why two sets?**  
  - Hitting a node in `visited` means a back-edge → cycle.  
  - `checked` avoids reprocessing subgraphs already proven acyclic.
- **Gotchas:** Keep the order `visited.remove(node)` then `checked.add(node)`. For very deep chains, consider Kahn’s BFS (topological sort) to avoid recursion limits.