#case1 찍수개수 - 짝수 번째에 W가 와야하고 
#case2 홀수 개수 - 홀수 번째에 w가 와야함.
class Solution:
    def oslo(self):
        n = int(input())
        for _ in range(n):
            t = int(input())
            initial_state = list(map(str,input().rstrip("\n")))
            target_state = list(map(str,input().rstrip("\n")))
            cnt = []
            for i in range(t):
                if initial_state[i] != target_state[i]:
                    cnt.append(initial_state[i])
            if not cnt:
                print(0)
            elif cnt.count("B") >= cnt.count("W"):
                print(cnt.count("B"))
            else:
                print(cnt.count("W"))
    

            
            
solution = Solution()
solution.oslo()