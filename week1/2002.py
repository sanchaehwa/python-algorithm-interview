#key(자동차 번호) - value(인덱스+1) -- 상대적인 위치 
class Solution():
    def carOverTaking(self,n:int,carIn:dict,carOut:dict)->int:
        out_orders = list(carOut.keys())
        print(out_orders)
        count = 0
        for i in range(0,len(out_orders)-1):
            now_in = carIn[out_orders[i]]
            print(i,now_in)
            for j in range(i+1, len(out_orders)):
                next_in = carIn[out_orders[j]]
                print(j,next_in)
                if next_in < now_in:
                    count +=1
                    break
        return count
n = int(input())
carIn = {input():i for i in range(n)}
carOut = {input():i for i in range(n)}
solution = Solution()
print(solution.carOverTaking(n,carIn,carOut))