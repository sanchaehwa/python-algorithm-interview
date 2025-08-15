
M = int(input())
N = int(input())
lst = []
t = [i**2 for i in range(1,101)]
for i in t:
    if M <= i <= N:
        lst.append(i)

if lst:
    print(sum(lst))
    print(min(lst))
else:
    print(-1)  

