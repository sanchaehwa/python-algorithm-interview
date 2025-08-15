class ListNode:
    def __init__(self,val = 0,next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseLinkedList(self,arr1:ListNode)->list:
        list_revers = []
        while arr1:
            list_revers.append(arr1.val)
            arr1 = arr1.next
        list_revers.reverse()
        return list_revers
def toLinkedList(arr):
    head = ListNode()
    curr = head
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return head.next
arr1 = list(map(int, input().split()))
l1 = toLinkedList(arr1)
solution = Solution()
print(solution.reverseLinkedList(l1))