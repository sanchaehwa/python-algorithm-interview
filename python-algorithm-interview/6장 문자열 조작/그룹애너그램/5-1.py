import ast
from typing import List
import collections

#애너그램 = 서로 문자 순서만 다른 단어들을 하나의 리스트로 묶는거

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list) #list 형태로 추가
        for word in strs:
            #정렬된 문자열을 Key로 삼고, 그룹화
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())

#strs = eval(input()) 
strs = ast.literal_eval(input())
solution = Solution()
print(solution.groupAnagrams(strs))