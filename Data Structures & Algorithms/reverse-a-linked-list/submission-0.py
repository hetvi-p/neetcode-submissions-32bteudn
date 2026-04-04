# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        prev = None
        while (curr is not None):
            next = curr.next
            head.next = prev
            print(head.val)
            prev = curr
            curr = next
            if curr is not None:
                head = curr
        
        return head

        