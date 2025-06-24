import sys
from itertools import permutations
class Solution:
    def isPalindrome(self)->None:
        #테스트케이스 개수
        T = int(sys.stdin.readline())
        for _ in range(T):
            words = []
            #펠린드롭 검사할 단어의 수 
            K = int(sys.stdin.readline())
            for _ in range(K):
                word = sys.stdin.readline().strip()
                words.append(word)
            # result = []
            # for i in range(K): #5
            #     for j in range(i +2, K + 1):
            #         sub = words[i:j]
            #         str_sub = ''.join(sub)
            #         if str_sub == str_sub[::-1]:
            #             result.append(str_sub)\
            result = []
            for w1,w2 in permutations(words,2):
                sub = w1+w2
                if sub == sub[::-1]:
                    result.append(sub)
            if not result:
                print(0)
            else:
                print(result[0])

                        
solution = Solution()
solution.isPalindrome()

