lst = []
for i in range(9):
    lst.append(int(input()))

lst.sort() #오름차순 정렬

sum_lst = sum(lst) 
for i in range(9):
    for j in range(i+1,9):
        if sum_lst - lst[i] - lst[j] == 100: #100이 되어야 함
            for k in range(9):
                if k == i or k == j:
                    pass 
                else:
                    print(lst[k])
            exit()

