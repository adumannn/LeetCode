# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        
        ans = ListNode()
        ans_t = ans

        while head:
            

            if head.val != val:
                ans_t.next = head
                ans_t = ans_t.next
            
            head = head.next

        ans_t.next = None
        return ans.next
                

