class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        val1 = 0
        val2 = 0
        carry = 0

        if l1:
            val1 = l1.val
            l1 = l1.next
        if l2:
            val2 = l2.val
            l2 = l2.next

        val = val1 + val2 + carry
        carry = val // 10
        val = val % 10
        head = ListNode(val)
        node = head

        while l1 or l2:
            val1 = 0
            val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            val = val1 + val2 + carry
            carry = val // 10
            val = val % 10
            node.next = ListNode(val)
            node = node.next

        if not carry == 0
            node.next = ListNode(carry)

        return head


if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    result = Solution().addTwoNumbers(l1, l2)

    while result:
        print(result.val)
        result = result.next

