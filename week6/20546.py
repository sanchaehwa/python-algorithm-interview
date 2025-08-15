'''
준현
- 한번 산 주식은 팔지않음
- 주식을 살 수 있다면 가능한 만큼 즉시 매수
성민
- 현금보다 주가가 높으면 주식을 사지않음
(1) 3일동안 가격이 연속으로 상승하면 4일은 하락할거댜 => 매도 (3일연속 그지점)
(2) 3일동안 가격이 연속으로 하락하면 4일은 상승  => 매수 (3일 연속 그 지점)
1-2 번 조건이면 전량 매수

[알고리즘]
준현 - 주식의 수 / 남은 돈 / 매수 
성민 - 주식의 수 / 남은 돈 / 매수 , 매도 

result = (남은 돈 1월 14일의 주가 × 주식 수)
'''
import sys
input = sys.stdin.readline

#보유하고 있는 돈
money = int(input())
#주가 리스트 14일
lst = list(map(int,input().split()))

#준현의 남은돈 
m1 = money
#주식의 수
cnt1 = 0

#성민의 남은돈
m2 = money
#주식의수
cnt2 = 0

for l in range(14):
    #준현이의 경우
    if lst[l] <= m1: #남은돈보다 주가가 낮은거 그럼 매수할수있음
        cnt1 += m1 // lst[l]
        m1 = m1 % lst[l]
for i in range(3,14): #연속성
    if lst[i-3] > lst[i-2] > lst[i-1]: #하락 구조 -- 매수
        if lst[i] <= m2:
            cnt2 += m2 // lst[i]
            m2 = m2 % lst[i]
    if lst[i-3]  < lst[i-2] < lst[i-1]: #상승 구조 -- 매도
        m2 += cnt2 * lst[i]
        cnt2 = 0 #주식수 초기화 == 매도
#14일 주가 + 남은돈 * 주식수
result1 = (lst[13]* cnt1) + m1
result2 = (lst[13]*cnt2) + m2



if result1 > result2:
    print("BNP")
elif result1 == result2:
    print("SAMESAME")
else:
    print("TIMING")
