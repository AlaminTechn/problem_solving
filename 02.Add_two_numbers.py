from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digits
            val = v1 + v2 + carry 
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs 
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        # Check if there's a remaining carry
        if carry:
            cur.next = ListNode(carry)

        return dummy.next

# Test case
l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

instance = Solution()
res = instance.addTwoNumbers(l1, l2)

# Print the result
while res:
    print(res.val, end=" ")
    res = res.next
