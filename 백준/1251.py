import sys

class Solution:
    def splitWord(self)->str:
        # #단어 입력 받고
        # word = input()
        # split1 = word[:2]
        # split2 = word[2:-2]
        # split3 = word[-2:]
        # #뒤집고
        # split1 = split1[::-1]
        # split2 = split2[::-1]
        # split3 = split3[::-1]
        # #합치고
        # target = split1 + split2 + split3
        # print(target)
        # #
        word = list(map(str, sys.stdin.readline().rstrip("\n")))
        print(word)
        target = []
        for i in range(1,len(word)-1):
            for j in range(i+1, len(word)):
                split1 = word[:i]
                split2 = word[i:j]
                split3 = word[j:]
                #뒤집어 
                split1.reverse()
                split2.reverse()
                split3.reverse()
                #합쳐
                target.append(("".join(split1+split2+split3)))
                #가장앞서는 가장 작은
        print(min(target))

solution = Solution()
solution.splitWord()
