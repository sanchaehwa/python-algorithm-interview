#문자열 받고 일단 문자열의 길이를 같게 만들어야해
class Solution:
    def string(self, word:str)-> int:
        str1,str2 = word.split(' ')
        str1_list = list(str1)
        str2_list = list(str2)

        cnt = 0
        result = []
        need = len(str2_list) - len(str1_list)
        if need != 0:
            slice_need = {(x, need - x) for x in range(need + 1)}
            for k,j in slice_need:
                process = str2_list[:k] + str1_list + str2_list[len(str2_list)-j:]
                # for i in range(len(str2_list)):
                #     if process[i] != str2_list[i]:
                #         cnt += 1
                #     result.append(cnt)
                #차이 계산
                cnt = sum(1 for a,b in zip(process,str2_list) if a!=b)
                result.append(cnt)
        else:
            cnt = sum(1 for a,b in zip(str1_list,str2_list) if a!=b)
            result.append(cnt)
        print(min(result))



word = input()

solution = Solution()
solution.string(word)