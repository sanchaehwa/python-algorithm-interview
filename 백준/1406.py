import sys
class DoublyListNode: #왼쪽으로 이동해야하니깐, 양방향 연결리스트
    def __init__(self,val=None,prev = None,next=None):
        self.val = val #현재의 노드 값
        self.prev = prev #이전 노드 값 *문자가 맨앞이면 prev가 None인 상태가 맞겠지
        self.next = next #다음 노드 값
class Editor:
    def __init__(self,text):
        self.head = DoublyListNode()
        self.tail = self.head
        self.cursor = self.tail

        for ch in text:
            self.insert(ch)
    #왼쪽 노드에 추가
    def insert(self,val):
        new_node = DoublyListNode(val)
        prev_node = self.cursor #cursor 오른쪽을 가리키고 있으니깐
        next_node = self.cursor.next

        prev_node.next = new_node 
        new_node.prev = prev_node
        new_node.next = next_node

        if next_node:
            next_node.prev = new_node
        else:
            self.tail = new_node
        self.cursor = new_node
    #왼쪽으로 커서를 옮김
    def moveLeft(self):
        if self.cursor.prev:
            self.cursor = self.cursor.prev
    #오른쪽으로 커서를 옮김
    def moveRight(self):
        if self.cursor.next:
            self.cursor = self.cursor.next
    #삭제
    def delete(self):
        if self.cursor != self.head:
            delete = self.cursor
            prev_node = delete.prev
            next_node = delete.next

            prev_node.next = next_node 
            if next_node:
                next_node.prev = prev_node
            else:
                self.tail = prev_node
            self.cursor = prev_node
    #출력 연결리스트 -> 리스트 -> join
    def printResult(self):
        result = []
        node = self.head.next
        while node:
            result.append(node.val)
            node = node.next
        return ''.join(result)
class Solution:
    def editor(self):
        text = list(sys.stdin.readline().strip())  # 초기 문자열
        editor = Editor(text)
        n = int(sys.stdin.readline())
        for _ in range(n):
            s = sys.stdin.readline().split()
            command = s[0]
            if command == "L": #커서를 왼쪽으로 한칸 옮김 - 커서가 문자의 맨앞이면 무시
                editor.moveLeft()
            elif command == "D":
                editor.moveRight()
            elif command == "B":
                editor.delete()
            elif command == "P": #왼쪽에 데이터 삽입
                editor.insert(s[1])
        print(editor.printResult())
def toLinkedList(arr:list)->DoublyListNode:
    head = DoublyListNode()
    curr = head
    for val in arr:
        newNode = DoublyListNode(val)
        curr.next = newNode 
        newNode.prev = curr #이전 노드
        curr = newNode
    return head.next #첫번째 노드 반환

solution = Solution()
solution.editor()


