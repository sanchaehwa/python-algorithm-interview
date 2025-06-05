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

from collections import Counter
def solution(word:str) -> str:
    counter = Counter(word)
    mid = ''
    half = []
    for char in sorted(counter.keys()):
        count = counter[char]
        print(count)
        if(count%2 == 1):
            print("I'm Sorry Hansoo")
            return
            mid = char
        half.append(char * (count //2))
    first_half = ''.join(half)
    palindrome = first_half + mid + first_half[::-1]
    print(palindrome)

word = input().strip()
solution(word)
        
