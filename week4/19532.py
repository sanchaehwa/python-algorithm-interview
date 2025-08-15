import sys
class Solution:
    def mathLecture(self)->None:
        # x,y = 0,0
        # a,b,c,d,e,f = map(int, sys.stdin.readline().split())
        # #식
        # x1 = a * d  #x값
        # y1  = b * d #y값
        # c1 = c * d 

        # x2 = d * a
        # y2 = e * a
        # c2 = f * a

        # result = []
        # if(x1 == x2):
        #     y = (c1 - c2)//(y1 - y2)
        #     x = (c - (b*y)) // a
        #     result.append(x)
        #     result.append(y)
        # print(' '.join(map(str, result)))
        a, b, c, d, e, f = map(int, input().split())
        x = (c*e - b*f) // (a*e - b*d)
        y = (a*f - c*d) // (a*e - b*d)

        print(x, y)

solution = Solution()
solution.mathLecture()