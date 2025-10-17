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
