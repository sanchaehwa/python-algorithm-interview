def solution(n,lst : list) -> int:
    for i in lst:
        score = 0
        current = 0
        for j in i:
            if j == 'O':
                current += 1
                score += current
            else:
                current = 0
        print(score)

                
n = int(input())
#한줄에 여러개,그런걸 n줄 입력 받을때
lst = [list(input().strip()) for _ in range(n)]
solution(n,lst)