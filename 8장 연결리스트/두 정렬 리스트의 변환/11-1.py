class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    def isPalindrome(self, values : list)->bool:
        #values 입력
        if not values:
            return True
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        q = []
        current = head
        while current:
            q.append(current.val)
            current = current.next
        return q == q[::-1]
solution = Solution()
values = list(map(int,input().split()))
print(solution.isPalindrome(values))