#Java => C++
#C++ => Java
#_ 가 포함되어있으면 C++ 이고, _가 포함되어있지않으면 Java -> Java에서 Lower로 바꾸고, * 대문자 기준으로 문자 나누고 lower 
import sys
import re
class Solution:
    def javaVsC(self,a:str)->str:
        result = []
        if a.find("_") != -1: #찾지못한경우는 -1 를반환 - C++ 
            result = a.split("_") 
            to_Java = result[0] + ''.join(i.capitalize() for i in result[1:]) #앞문자는 그대로 
            print(to_Java)
        else: #java 인경우
            result = re.findall(r'[A-Z]?[a-z]+',a)
            result = [i.lower() for i in result if i]
            to_C = '_'.join(result)
            print(to_C)

a = sys.stdin.readline().strip() # /n 제거
solution = Solution()
solution.javaVsC(a) 