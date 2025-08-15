#기본값 설정
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
#병합 정렬 - 재귀 구조로 풀기 **
class Solution:
    def mergeTwoList(self,arr1:ListNode,arr2:ListNode):
        #연결 리스트는 위치 기반
        if not arr1 or arr2 and arr1.val > arr2.val: #arr1 왼쪽, arr2 오른쪽
            #스왑 
            arr1,arr2 = arr2,arr1
        if arr1:
            #재귀 - 병합
            arr1.next = self.mergeTwoList(arr1.next, arr2) 
        return arr1
#(입력) 리스트 -> 연결리스트
def build_linked_list(arr):
    head = ListNode()
    curr = head
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return head.next
#(출력) 연결리스트 -> 리스트 
def print_list(node):
    while node:
        print(node.val, end=' ')
        node = node.next
    print()    

#값을 입력받는 부분
arr1 = list(map(int,input().split()))
l1 = build_linked_list(arr1)

arr2 = list(map(int,input().split()))
l2 = build_linked_list(arr2)

solution = Solution()
merged = solution.mergeTwoList(l1,l2)
print(print_list(merged))
