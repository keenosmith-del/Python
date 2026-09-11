class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self,
        l1: ListNode | None,
        l2: ListNode | None
    ) -> ListNode | None:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0

            total = value1 + value2 + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next


def create_linked_list(values):
    dummy = ListNode(0)
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def linked_list_to_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


solution = Solution()

l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])

print(linked_list_to_list(solution.addTwoNumbers(l1, l2)))
# [7, 0, 8]

l1 = create_linked_list([0])
l2 = create_linked_list([0])

print(linked_list_to_list(solution.addTwoNumbers(l1, l2)))
# [0]

l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = create_linked_list([9, 9, 9, 9])

print(linked_list_to_list(solution.addTwoNumbers(l1, l2)))
# [8, 9, 9, 9, 0, 0, 0, 1]
