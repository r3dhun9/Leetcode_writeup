class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        tail = None
        num1 = ''
        num2 = ''
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        out = int(num1[::-1]) + int(num2[::-1])
        strout = str(out)[::-1]
        tail = ListNode(int(strout[0]))
        head = tail
        for i in range(1, len(strout)):
            newnode = ListNode(int(strout[i]))
            tail.next = newnode
            tail = tail.next
        return head
