#금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력. 대소문자 구분을 하지 않으며, 구두점 무시 (숫자랑 문자)
from typing import List
import collections
import re

class Solution:
    def mostCommonwords(self,paragraph:str,banned:List[str]) -> str:
        #대 소문자 구분을 하지않으며 -> 소문자 , 구두점 무시 
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
                    if word not in banned]
        counts = collections.defaultdict(int)
        for word in words:
            counts[word] += 1
        return max(counts, key=counts.get)

paragraph = input()
banned = eval(input())
solution = Solution()
print(solution.mostCommonwords(paragraph,banned))