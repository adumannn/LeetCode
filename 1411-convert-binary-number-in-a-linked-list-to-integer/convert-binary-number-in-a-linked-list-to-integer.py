# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        cnt = 0
        while head:
            cnt = cnt * 2 + head.val
            head = head.next

        return cnt