# from itertools import permutations
# def solution(word: str) -> list:
#     #문자열을 배열로 
#     alphabet_list = []
#     isPalindrome = []
#     #가능한 순열
#     #perm = set(permutations([alphabet for alphabet in word])) *O(n! * n)
#     for p in perm:
#         alphabet_list.append(''.join(p))
#     for i in alphabet_list:
#         if i == i[::-1]:
#             isPalindrome.append(i)
#     if not isPalindrome: #리스트가 비어있다는것은 - 펠린드롬이 없는것
#         print("I'm Sorry Hansoo")
#         return
    
#     isPalindrome.sort()
#     print(isPalindrome[0])    

# word = input()
# solution(word)

# from collections import Counter
# def solution(word:list) -> str:
#     counter = Counter(word)
#     odd_count = 0
#     center = ''
#     half = []
#     for ch in sorted(counter): #사전순으로 정렬
#         print(ch)
#         count = counter[ch]
#         #홀수면 펠리드롭 안됨
#         if count % 2 == 1:
#             odd_count += 1
#             center = ch
#             if odd_count > 1:
#                 print("I'm Sorry Hansoo")
#         half.append(ch * (count // 2))
#     half_str = ''.join(half)
#     print(half)
#     print(half_str + center + half_str[::-1])

# word = input()   
# solution(word)



        
def solution(name:str)->str:
    count = dict()
    keys = sorted(list(set(name))) #사전순 정렬
    odd = []
    for key in keys:
        cnt = name.count(key)
        count[key] = cnt
        if cnt % 2:
            odd.append(key)
    if len(odd) > 1:
        print("I'm Sorry Hansoo")
        return
    else:
        result = ''
        for key in keys:
            result += key * (count[key] // 2)
        if odd:
            result += odd[0] + result[::-1]
        else:
            result += result[::-1]
    print(result)

name = input()
solution(name)
