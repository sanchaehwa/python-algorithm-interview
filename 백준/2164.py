# import sys
# class Solution:
#     def card2(self):
#         #N장의 카드
#         n = int(sys.stdin.readline())
#         card = [i for i in range(1,n+1)]
#         for i in range(n-1):
#             #맨 앞 카드는 제거
#             card.pop()
#             #맨 뒤에 다음 카드 추가
#             card.append(card[i+1])
#         if len(card) == 1:
#             print(i)
# solution = Solution()
# solution.card2()
import sys
class ListNode:
    def __init__(self,val=None,prev=None,next=None):
        self.val = val
        self.prev = prev
        self.next = next
#맨앞카드는 제거
class Cards:
    def __init__(self,card):
        self.head = None
        self.tail = None

    def append(self,val):
        new_node = ListNode(val)
        if not self.head: #리스트가 비어있는경우 
            self.head = self.tail = new_node
            new_node.next = new_node.prev = new_node
        else: #리스트가 비어있지않는 경우
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node #마지막요소로 
    def pop_front(self):
        if self.head == self.tail: #맨처음, 마지막 노드가 같다 = > 하나만 남은 노드
            val = self.head.val
            self.head = self.tail = None #초기화
            return val
        val = self.head.val
        self.head = self.head.next
        #이전 노드
        self.head.prev = self.tail
        self.tail.next = self.head
        return val
    def move_front_to_back(self):
            if self.head != self.tail:
                self.head = self.head.next
                self.tail = self.tail.next

    def get_only_node_value(self):
        return self.head.val if self.head else None:
    
class Solution:
    def card2(self):
        n = int(sys.stdin.readline())
        dq = Cards()
        for i in range(1, n + 1):
            dq.append(i)

        while dq.head != dq.tail:
            dq.pop_front()          # 맨 앞 제거
            dq.move_front_to_back() # 그 다음 맨 뒤로

        print(dq.get_only_node_value())
solution = Solution()
solution.card2()