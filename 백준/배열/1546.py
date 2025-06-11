class Solution():
    def testAverage(self,n:int,score:list)->float:
        total = 0
        highScore = max(score)
        for i in score:
            newScore = i/highScore*100
            total += newScore
        average = total / n
        print(average)

    
n = int(input())
score = list(map(int,input().split()))
solution = Solution()
solution.testAverage(n,score)



