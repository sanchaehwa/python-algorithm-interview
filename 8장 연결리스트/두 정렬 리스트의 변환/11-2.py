class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q = []
        while head:
            q.append(head.val)
            head = head.next
        return q == q[::-1]