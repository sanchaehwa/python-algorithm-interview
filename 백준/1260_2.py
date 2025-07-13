import sys
A = int(sys.stdin.readline())
B = list(map(int,sys.stdin.readline().strip()))
lst = []
for i in B:
    lst.append(i*A)
lst.reverse()
for i in lst:
    print(i)
Ba = int(''.join(map(str,B)))
print(Ba * A)