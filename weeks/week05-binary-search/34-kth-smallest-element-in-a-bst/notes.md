# Notes

## Link
https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

## Approach
1. Perform an **in-order traversal (Left → Node → Right)** on the BST.  
   - Because BST’s in-order traversal produces nodes in ascending order.  
2. Store the visited node values in a list (`box`).  
3. Return the (k-1)-th element from the list.

## Code
``` python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

def dfs(node, box):
    if node.left:
        dfs(node.left, box)
    box.append(node.val)
    if node.right:
        dfs(node.right, box)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        box = deque([])
        dfs(root, box)
        return box[k-1]
```

## Complexity Analysis
- **Time:** O(n) — Each node is visited once during traversal.  
- **Space:** O(n) — Recursion stack and the list for storing nodes.

## Review
- In a **Binary Search Tree**, the in-order traversal gives all nodes in **sorted order**.  
- That’s why taking the (k-1)-th element directly gives the k-th smallest value.  
- Other traversal types:
  - **Pre-order (Node → Left → Right):** Visits root first; used for copying or serializing a tree.  
  - **In-order (Left → Node → Right):** Produces sorted order for BSTs.  
  - **Post-order (Left → Right → Node):** Useful for deleting nodes or evaluating expressions.  
  - **Level-order (Breadth-First):** Traverses layer by layer; used in shortest path or breadth-first searches.
- Simple and intuitive method, though it can be optimized with iterative DFS or early stopping when `k` is reached.
