from typing import List
import ast
class Solution:
    def reorderLogFilters(self, logs:List[str])->List[str]: #반환 값 list
        #로그가 숫자인지 문자인지 확인
        letters, digits = [],[]
        for log in logs:
            if log.split()[1].isdigit(): #숫자
                digits.append(log)
            #문자
            else:
                letters.append(log)
        #letters만 
        letters.sort(key=lambda x: (x.split()[1:],x.split()[0]))
        return letters + digits

#logs = eval(input())
logs = ast.literal_eval(input())
solution = Solution()
print(solution.reorderLogFilters(logs))