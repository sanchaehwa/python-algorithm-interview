# T = int(input())
# for _ in range(T):
#     a,b,c = map(int,input().split())
#     lst = []
#     for i in range(1,61):
#         if 1  <= i <= a:
#             x = i
#         if 1 <= i <= b:
#             y = i
#         if 1 <= i <= c:
#             z = i
#         if (x % y) == (y % z) == (z % x):
#             lst.append([x,y,z])
#     print(len(lst))

T = int(input())
while T > 0 :
    a, b, c = map(int, input().split())
    print(min(a, min(b, c)))
    T -= 1
