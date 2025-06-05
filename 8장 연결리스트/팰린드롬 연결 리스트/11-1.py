
from typing import Deque
from collections import deque

class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode)->bool:
        #정적 타입 힌트를 사용
        q : Deque[int] = deque()
        if not head:
            return True
        node = head
        while node:
            q.append(node.val)
            node = node.next
        while len(q)>1: #1이면 그냥 True*앞뒤 비교할필요도 없음
            if q.popleft() != q.pop():
                return False
        return True
#연결리스트 생성 (정수 리스트 -> 전체 연결리스트)
def build_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

arr = list(map(int, input().split()))
head = build_linked_list(arr)
solution = Solution()
print(solution.isPalindrome(head))