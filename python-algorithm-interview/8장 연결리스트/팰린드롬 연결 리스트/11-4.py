from typing import List

class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution():
    def isPalindrome(self, head : ListNode) -> bool:
        rev = None #역순으로 만들 연결리스트
        slow = fast = head # 같은 시작점에서
        while fast and fast.next:
            fast = fast.next.next #두칸이동
            rev, rev_next, slow = slow, rev, slow.next #한칸이동
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow,rev = slow.next, rev.next
        return not rev

def build_linked_list(arr):
    dummy = ListNode()
    #리스트 -> 연결 리스트
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

arr = list(map(int, input().split()))
head = build_linked_list(arr)
solution = Solution()
print(solution.isPalindrome(head))