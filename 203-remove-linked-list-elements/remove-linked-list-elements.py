class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, target):

        while head is not None and head.val == target:
            head = head.next
        
        current = head

        while current and current.next:
            if current.next.val == target:
                current.next = current.next.next
            else:
                current = current.next

        return head
        