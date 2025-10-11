# Notes

## Link
https://leetcode.com/problems/palindrome-linked-list/description/

## Approach
1. Use two helper functions:
   - `halfNode(node)`: Finds the midpoint of the linked list using the slow–fast pointer approach.
   - `reverseList(node)`: Reverses a linked list and returns the new head.
2. Find the middle of the list using `halfNode()`.
3. Reverse the second half of the list using `reverseList()`.
4. Compare the first and second halves node by node.
5. If all corresponding values match, it is a palindrome.

## Code
``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseList(node):
    prev = None
    curr = node
    while curr:
        next_node = curr.next       # 1. store the next node
        curr.next = prev            # 2. reverse direction
        prev = curr                 # 3. move prev forward
        curr = next_node            # 4. move curr forward
    return prev                     # new head after reverse

def halfNode(node):
    slow, fast = node, node
    while fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
    return slow                     # slow stops at the first half's end

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step 1: Find half of the list
        half = halfNode(head)

        # Step 2: Reverse the second half
        half = reverseList(half.next)

        # Step 3: Compare both halves
        while head and half:
            if head.val != half.val:
                return False
            head, half = head.next, half.next
        return True
```

## Complexity Analysis
- Time: `O(n)`: Each node is visited at most twice (find half + reverse + compare).
- Space: `O(n)`: All operations are done in-place without additional structures.

## Review
- `halfNode()` is used to split the list into two halves using slow–fast pointer technique.
    - `fast` moves two steps per iteration while slow moves one.
    - When `fast` reaches the end, `slow` will be at the midpoint.
    - This works because for every two steps fast takes, `slow` moves one, effectively marking the center when traversal ends.
    - Returning `slow` gives a pointer to the last node of the first half, so that we can later reverse starting from `slow.next`.
- `reverseList()` iteratively reverses the linked list starting from a given node.
    - Keeps track of three pointers: `prev`, `curr`, and `next_node`.
    - Each iteration flips the `.next` pointer of the current node toward the previous one.
    - `prev` always points to the head of the reversed section built so far.
    - When traversal ends, `prev` becomes the new head of the reversed half.
    - It’s done in-place, meaning no extra memory except a few variables.
- The final comparison checks symmetry node by node between the head and reversed half.
    - If all pairs match, it’s a palindrome; otherwise, return False immediately.
- Key takeaway:
    - The combination of two-pointer midpoint detection + in-place reversal gives a memory-efficient `O(n)` solution.
    - The structure is modular: each helper function does one clear job, improving both readability and debugging.
