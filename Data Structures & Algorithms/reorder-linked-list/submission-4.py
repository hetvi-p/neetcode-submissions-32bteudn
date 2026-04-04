# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        first = head
        length = 0
        while (first != None):
            first = first.next
            length += 1
        first = head
        for i in range(length//2):
            first = first.next

        prev = None
        while (first != None):
            next = first.next
            first.next = prev
            prev = first
            first = next
    
        first = prev

        new = ListNode()
        dummy = new

        for i in range(length//2):
            new.next = head
            head = head.next
            new = new.next
            new.next = first
            first = first.next
            new = new.next

        head = dummy.next

