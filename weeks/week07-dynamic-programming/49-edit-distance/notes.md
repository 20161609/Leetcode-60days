# Notes

## Link
https://leetcode.com/problems/edit-distance/description/

## Approach
1. Define `dp[i][j]` = **minimum operations** to convert `word1[:i]` → `word2[:j]`.
2. Base cases:
   - `dp[i][0] = i` (delete all `i` chars)
   - `dp[0][j] = j` (insert all `j` chars)
3. Transition for `i ≥ 1, j ≥ 1`:
   - If `word1[i-1] == word2[j-1]`: `dp[i][j] = dp[i-1][j-1]`
   - Else take the min of:
     - **Insert:** `dp[i][j-1] + 1`
     - **Delete:** `dp[i-1][j] + 1`
     - **Replace:** `dp[i-1][j-1] + 1`

## Code
``` python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(m+1):
            dp[i][0] = i  # delete all
        for j in range(n+1):
            dp[0][j] = j  # insert all

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i][j-1] + 1,   # insert
                        dp[i-1][j] + 1,   # delete
                        dp[i-1][j-1] + 1  # replace
                    )
        return dp[m][n]
```

## Complexity Analysis
- **Time:** O(m·n)
- **Space:** O(m·n)  *(can be reduced to O(n) with rolling rows)*

## Review
- Invariant: `dp[i][j]` stores the **minimum edits** for prefixes `word1[:i]` and `word2[:j]`.
- The three neighbors map directly to the three operations:
  - left → **insert** (make `word2[j-1]` appear)
  - up → **delete** (drop `word1[i-1]`)
  - diagonal → **replace** (or **match** if equal)
- Base rows/cols mean “delete all” or “insert all” when one side is empty.
- What I struggled with: seeing why each operation corresponds to that neighbor.  
  Thinking in **prefixes** makes it clear: adding/removing/replacing one last char moves you left/up/diag in the table.
- Tips: if chars match, just copy diagonal; otherwise take `min(left, up, diag) + 1`.  
  Rolling arrays can cut space to O(n).
