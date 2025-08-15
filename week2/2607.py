import sys
from collections import Counter,defaultdict
from math import comb
class Solution:
    def sameWord(self):
        #단어수
        N = int(sys.stdin.readline())
        word = [list(sys.stdin.readline().strip()) for _ in range(N)]
        cnt = 0
        #조건1 같은 구성을 갖는 경우
        for i in range(1,N):
            word1 = word[0]
            word2 = word[i]
            #한문자를 더해서 같아지는 경우 * 조건2
            c1 = Counter(word1)
            c2 = Counter(word2)
            #완전히 같은 경우
            if c1 == c2:
                cnt += 1
                continue
            if sum((c1 - c2).values()) == 1 and sum((c2-c1).values())==0:#하나만 모자라니깐 하나를 더해주면 
                cnt += 1
                continue
            if sum((c2 - c1).values()) == 1 and sum((c1 - c2).values()) == 0:
                cnt += 1
                continue
            #교체해서 같은 경우
            if sum((c2 - c1).values()) == 1 and sum((c1-c2).values()) == 1:
                cnt += 1
                continue
        print(cnt)
                
solution = Solution()
solution.sameWord()