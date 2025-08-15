import sys
input = sys.stdin.readline



student = []
for _ in range(28):
    student.append(int(input()))
    
school = [0] * 31
for s in student:
    school[s] = s
for i in range(1,31):
    if school[i] == 0:
        print(i)


