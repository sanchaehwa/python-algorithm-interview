import sys

class Solution:
    def stableWord(self, word: list):
        result = []

        for line in word:
            count_word = {'{': 0, '}': 0} 
            for ch in line:
                if ch in ['{', '}']:
                    count_word[ch] += 1

            open_count = count_word['{']
            close_count = count_word['}']

            # case1: {, } 1개씩
            if open_count == 1 and close_count == 1:
                result.append(2)
            # case2: 짝 맞음
            elif open_count == close_count:
                result.append(0)
            # case3: 개수 다름
            else:
                #abs 절댓값 - + 상관없이
                result.append(abs(open_count - close_count) // 2)
        
        for m in range(len(result)):
            print(m+1,'. ',result[m],sep='')

word = []
while True:
    lst = sys.stdin.readline().strip()
    if "-" in lst:
        break
    word.append(lst)

solution = Solution()
solution.stableWord(word)