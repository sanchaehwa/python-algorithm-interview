import sys
class Solution:
    def wheelOfFortune(self):
        #바퀴의 수 - 바퀴를 돌리는 횟수
        wheel = list(map(int,sys.stdin.readline().split()))
        n = wheel[0]
        r = wheel[1]
        #종이
        p = ["?"] * n  #["?","?","?"]
        #현재위치 저장
        used = dict()
        now = 0
        for _ in range(r):
            peek = list(map(str,sys.stdin.readline().split()))
            rotate = int(peek[0])
            a = peek[1]
            #현재위치에서 rotate한거만큼 이동
            now = (rotate + now) % n
            #이동하고자하는 위치에 다른 문자가 있으면 충돌
            if p[now] != "?" and p[now] != a:
                print("!")
                exit()
            #다른 위치에서도 해당문자가 있으면 충돌
            if a in used and used[a] != now:
                print("!")
                exit()
            #일반적인 경우
            p[now] = a
            used[a] = now
        #현재 위치에서 시계 방향으로
        for i in range(n):
            print(p[(now-i) % n],end="")

solution = Solution()
solution.wheelOfFortune()