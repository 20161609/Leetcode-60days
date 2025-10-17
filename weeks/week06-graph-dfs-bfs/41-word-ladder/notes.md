# Notes

## Link
https://leetcode.com/problems/word-ladder/

## Approach
- **Pattern trick (new to me):** For each word, replace one character with `*` to make a **pattern** (e.g., `hot` → `*ot`,`h*t`,`ho*`).  
  Use a `defaultdict(list)` to map each pattern → all words that fit it.
- **BFS:** Start from `beginWord` with depth `1`.  
  For the current word, generate its patterns and push all unseen neighbors from those pattern lists.  
  First time we pop `endWord`, return the depth.

## Code
``` python
from collections import deque
from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        try:
            wordList.index(endWord)
        except:
            return 0

        box = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                box[word[:i:]+'*'+word[i+1::]].append(word)

        queue, visited = deque([(beginWord, 1)]), set([beginWord])
        while queue:
            word, depth = queue.popleft()
            if word == endWord:
                return depth
            
            for i in range(len(word)):
                for nxt in box[word[:i:]+'*'+word[i+1::]]:
                    if not nxt in visited:
                        queue.append((nxt, depth + 1))
                        visited.add(nxt)
        return 0
```

## Complexity Analysis
Let `n` be the total number of pattern slots, i.e., `n = (#words × word_length)`.
- Time: `O(n)` to build the pattern map + `O(n)` for BFS over patterns/edges → `O(n)`.  
- Space: `O(n)` for the pattern map + queue/visited.

## Review
- The `pattern index` is the key idea: it turns “one-letter different” checks into **O(1)-ish** lookups via patterns.
- `visited` avoids revisiting words; BFS guarantees the shortest ladder length.
- Micro-opts:
  - After expanding a pattern, you can clear its list (`box[pat] = []`) to avoid re-scanning it later.
  - Pre-check `endWord` with a `set` (not `list.index`) for faster membership.
