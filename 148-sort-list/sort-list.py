class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head

        size = 0
        curr = head
        while curr is not None:
            size += 1
            curr = curr.next

        width = 1

        while width < size:
            curr = head
            prev = None

            while curr is not None:
                left = curr
                right = left
                left_count = 0

                for _ in range(width):
                    if right is None:
                        break
                    right = right.next
                    left_count += 1

                rest = right
                right_count = 0

                for _ in range(width):
                    if rest is None:
                        break
                    rest = rest.next
                    right_count += 1

                while left_count > 0 or right_count > 0:
                    if left_count == 0:
                        take_left = False
                    elif right_count == 0:
                        take_left = True
                    else:
                        take_left = left.val <= right.val

                    if take_left:
                        chosen = left
                        left = left.next
                        left_count -= 1
                    else:
                        chosen = right
                        right = right.next
                        right_count -= 1

                    if prev is None:
                        head = chosen
                    else:
                        prev.next = chosen

                    prev = chosen

                curr = rest

            prev.next = None
            width *= 2

        return head