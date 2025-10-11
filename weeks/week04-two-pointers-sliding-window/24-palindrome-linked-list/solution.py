# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverseList(node):
    prev = None
    curr = node

    while curr:
        next_node = curr.next   # 1. store the next node
        curr.next = prev        # 2. reverse direction properly
        prev = curr             # 3. move prev forward
        curr = next_node        # 4. move curr forward

    return prev  # new head

def halfNode(node):
    slow, fast = node, node
    while fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
    return slow

def printNode(node):
    while node:
        print(node.val)
        node = node.next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step1: Find Half
        half = halfNode(head)

        # Step2: Reverse over half
        half = reverseList(half.next)

        # Step3: Compare head and half
        while head and half:
            if head.val != half.val:
                return False
            head, half = head.next, half.next
        return True