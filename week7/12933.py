import sys
input = sys.stdin.readline


word = list(input().strip())
target = "quack"
duck_states = [] #상태코드 

#1. q부터 시작해야하고 -- quack 를 만들수 있는가? -- 만들수있다 하면 
max_ducks = 0 #오리수
for w in word:
    placed = False
    for i in range(len(duck_states)):
        if target[duck_states[i]] == w:
            duck_states[i] += 1
            if duck_states[i] == 5:
                duck_states[i] = 0  # 한 마리 완성되면 초기화하여 재사용 가능
            placed = True
            break
    if not placed and w == 'q':
            duck_states.append(1) #새 오리를 넣고 시작하고
            max_ducks = max(max_ducks,len(duck_states))
    elif not placed: #처음 시작이 q가 아닌 경우에는
        duck_states.append(-1)

if -1 in duck_states or any(state != 0 for state in duck_states):
    print(-1) #만들수 없는 경우
else:
    print(max_ducks)
        

