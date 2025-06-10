class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
        def reverseList(self, head1: ListNode, head2: ListNode) -> None:
        # 역순 변환 함수
            def reverse(node: ListNode, prev: ListNode = None):
                if not node:
                    return prev
                next, node.next = node.next, prev
                return reverse(next, node)

        # 연결리스트 -> 리스트
        def toList(node: ListNode):
            result = []
            while node:
                result.append(node.val)
                node = node.next
            return result

        reverse_head1 = reverse(head1)
        reverse_head2 = reverse(head2)

        num1 = int(''.join(map(str, toList(reverse_head1))))
        num2 = int(''.join(map(str, toList(reverse_head2))))
        num = num1 + num2
        
        #807를 다시 역순 연결리스트 - 노드
        def answerToLinkedList(num):
            dummy = ListNode
            current = dummy
            for val in str(num)[::-1]:
                current.next = ListNode(int(val))
                current = current.next
            return dummy.next
        answer = answerToLinkedList(num)
        print(toList(answer))
# 리스트 -> 연결리스트
def toLinkedList(arr):
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# 입력
li1 = list(map(int, input().split()))  # 예: 1 2 3
li2 = list(map(int, input().split()))  # 예: 4 5 6
head1 = toLinkedList(li1)
head2 = toLinkedList(li2)
solution = Solution()
solution.reverseList(head1, head2)