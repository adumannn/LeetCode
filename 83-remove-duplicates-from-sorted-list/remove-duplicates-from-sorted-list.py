# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None

        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                dup = curr.next
                curr.next = dup.next   
            else:
                curr = curr.next

        return head