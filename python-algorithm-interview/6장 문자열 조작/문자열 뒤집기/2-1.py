#입력값은 문자 배열이며,리턴 없이 리스트 내부를 직접 조작

#사용자 입력을 파이썬 객체 - 입력값이 리스트 형식이니깐
words = eval(input())
def solution(words):
    #투 포인터, 범위를 조절해나가면서 풀이 (s 내불를 스왑)
    left,right = 0,len(words)-1
    while left < right:
        words[left],words[right] = words[right],words[left]
        left += 1
        right -=1
    return words
print(solution(words))
    
