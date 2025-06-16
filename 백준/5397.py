import sys
# 양방향 연결리스트 
class DoublyListNode:
    def __init__(self,val=None,prev=None,next=None):
        self.val = val
        self.prev = prev
        self.next = next
class Key:    
    def __init__(self):
        self.head = DoublyListNode()
        self.tail = self.head
        self.cursor = self.tail
    #알파벳이면 Insert
    def insert(self,val):
        new_node = DoublyListNode(val)
        prev_node = self.cursor
        next_node = self.cursor.next

        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = next_node

        if next_node:
            next_node.prev = new_node
        else:
            self.tail = new_node
        self.cursor = new_node
    
    #왼쪽 이동
    def moveLeft(self):
        if self.cursor.prev:
            self.cursor = self.cursor.prev
    #오른쪽 이동
    def moveRight(self):
        if self.cursor.next:
            self.cursor = self.cursor.next
    #백스페이스 , 삭제
    def delete(self):
        if self.cursor != self.head:
            delete = self.cursor #커서 앞의 문자를 지운다
            prev_node = delete.prev
            next_node = delete.next

            prev_node.next = next_node
            if next_node:
                next_node.prev = prev_node
            else:
                self.tail = prev_node 

    #출력
    def printResult(self):
        result = []
        node = self.head.next
        while node:
            result.append(node.val)
            node = node.next
        return ''.join(result)

class Solution:
    def keyLogger(self):
        #문자의 개수
        n = int(sys.stdin.readline())
        for _ in range(n):
            password = list(sys.stdin.readline().strip())
            key = Key()
            for i in password:
                if i == "<": #왼쪽이동
                    key.moveLeft()
                elif i == ">": #오른쪽 이동
                    key.moveRight()
                elif i == "-": #삭제
                    key.delete()
                else:
                    key.insert(i)
            print(key.printResult())

solution = Solution()
solution.keyLogger()
