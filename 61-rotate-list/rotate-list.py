# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:   
        if head is None or head.next is None:
            return head

        length = 1
        rightmost = head

        while rightmost.next is not None:
            rightmost = rightmost.next
            length += 1

        k %= length
        if k == 0:
            return head

        front_right = head
        for _ in range(length - k - 1):
            front_right = front_right.next

        new_head = front_right.next

        front_right.next = None
        rightmost.next = head

        return new_head