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