class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head:ListNode) -> ListNode:
        node,prev = head,None
        while node:
            next,node.next = node.next,prev
            prev,node = node,next
        return prev
    def toList(self, node:ListNode) ->list:
        result : list = []
        while node:
            result.append(node)
            node = node.next
        return result
    def toLinkedList(self, result:str)->ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node
    def addTwoNumvers(self,l1:ListNode,l2:ListNode)->ListNode:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))
        resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))
        return self.toLinkedList(str(resultStr))

