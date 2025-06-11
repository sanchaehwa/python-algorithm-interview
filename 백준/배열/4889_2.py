class Solution:
    def stableWord(self):
        cnt = 0
        while True:
            ans = 0
            result = []
            s = input()
            if s.startswith('-'):
                break
            for i in s:
                if i == "{":
                    result.append(i)
                else:
                    if result:
                        result.pop()
                    else:
                        result.append('{')
                        ans += 1
            ans += len(result) // 2
            cnt += 1
            print(f'{cnt}. {ans}')

solution = Solution()
solution.stableWord()