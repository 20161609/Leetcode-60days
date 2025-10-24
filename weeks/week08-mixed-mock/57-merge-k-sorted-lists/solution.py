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
