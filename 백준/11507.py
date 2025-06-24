#문양은 4개 
#총 카드의 수는 52개
#한 종류가 가지고 있는 카드의 수는 -> 52/4: 13
import sys
class Solution:
    def cardSet(self)->None:
        s = sys.stdin.readline().strip()
        card = {'P':[],'K':[],'H':[],'T':[]}
        #3덩어리씩 잘라
        chunks = [s[i:i+3] for i in range(0,len(s),3)]
        for i in chunks:
            if i[0] in card:
                card[i[0]].append(int(i[1:]))
        result = []
        for key,values in card.items():
            cnt = 13 - len(values)
            if len(values) != len(set(values)):
                print("GRESKA")
                return
            result.append(cnt)
        print(' '.join(map(str,result)))
        
solution = Solution()
solution.cardSet()


