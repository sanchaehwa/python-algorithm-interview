#재귀
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head:ListNode):
        def reverse(node:ListNode,prev:ListNode=None):
            if not node:
                return prev
            next, node.next = node.next,prev
            return reverse(next,node) #재귀
        return reverse(head)