# Notes

## Link
https://leetcode.com/problems/merge-k-sorted-lists/description/

## Approach
1. Traverse all input lists and collect node values into an array.
2. Sort the array.
3. Build a new linked list by iterating the sorted values.

## Code
``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        a = []
        for l in lists:
            while l: 
                a.append(l.val)
                l = l.next
        a.sort()
        answer = ListNode(-1)
        node = answer
        for i in a:
            node.next = ListNode(i)
            node = node.next
        return answer.next
```

## Complexity Analysis
- Time: O(n log n) due to sorting all values.
- Space: O(n) for the auxiliary array of values. (Output list not counted.)

## Review
- Straightforward and easy to implement.
- Uses extra memory and pays sorting cost.
- More optimal approaches:
  - Min-heap k-way merge: O(n log k) time, O(k) space.
  - Divide-and-conquer pairwise merge: O(n log k) time, O(1) extra space aside from recursion.
- Handles empty lists naturally; returns None when no nodes exist.
