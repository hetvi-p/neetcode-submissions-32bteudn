# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        rem = ListNode()
        rem.next = head
        res = rem
        i = 0

        

        while curr is not None:
            curr = curr.next
            i += 1
            if i > n:
                rem = rem.next
   
        rem.next = rem.next.next

        return res.next


        


        