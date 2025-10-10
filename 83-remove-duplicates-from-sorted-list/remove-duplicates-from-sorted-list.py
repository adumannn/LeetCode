class Solution(object):
    def deleteDuplicates(self, head):

        seen = set()
        duplicates = set()
        current = head

        while current:
            if current.val in seen:
                duplicates.add(current.val)
            else:
                seen.add(current.val)
            
            current = current.next

        seen_srt = sorted(seen)

        dummy = ListNode(0)
        curr = dummy
        for val in seen_srt:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next


        