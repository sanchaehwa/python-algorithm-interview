# 주어진 문자열이 펠린드롬인지 확인 대 소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 함
# 입력 : "A man, a plan, a canal: Panama "

s = input()
def solution(s):
    answer = []
    #1. 리스트로 변환 , 소문자로 변환, 영문자와 숫자만을 대상 (isalnum)
    for word in s:
        if word.isalnum():
            answer.append(word.lower())
    # 팰러드롬인지 확인
    while len(answer) > 1:
        if answer.pop(0) != answer.pop(): #처음과 끝을 비교
            return False
    return True
print(solution(s))