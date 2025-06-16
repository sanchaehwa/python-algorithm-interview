class Solution:
    def ring2(self):
        s = input().rstrip() #rstrip : 문자열에 오른쪽 공백이나 인자가 된 문자열의 모든 조합을 제거
        cnt = 0 #반지 개수
        for _ in range(int(input())):
            ring = input() 
            for _ in range(len(ring)):
                ring = ring[1:] + ring[0]
                if ring.find(s) >= 0: #find 위치를 찾는 함수
                    cnt += 1
        print(cnt)
solution = Solution()
solution.ring2()