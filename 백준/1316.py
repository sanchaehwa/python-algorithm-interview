#한줄 입력받고 한줄 검사하는 방식을 사용
class Solution:
    def groupWordCheck(self)->int:
        n = int(input())
        cnt = n
        for _ in range(n):
            word = input()
            for j in range(0,len(word)-1):
                if word[j] == word[j+1]:#그룹 단어
                    pass
                elif word[j] in word[j+1:]:#그룹 단어가 뒤에도 있는경우
                    cnt -=1
                    break
        print(cnt)

solution = Solution()
solution.groupWordCheck()
