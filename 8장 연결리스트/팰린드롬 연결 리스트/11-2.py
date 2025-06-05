from typing import List

class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution():
    def isPalindrome(self, head : ListNode) -> bool:
        q : List = [] #연결리스트의 노드들을 저장할 리스트
        if not head: #비교할 값이 없다는것 - 
            return True
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next
        while len(q)>1:
            if q.pop(0) != q.pop():
                return False
        return True

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