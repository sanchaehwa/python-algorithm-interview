import sys
#조건 검사
def checkpwd(word:str)->bool:
		#set으로 단 하나의 값에 여러 요소를 저장하는데, 중복값은 허용 안함
		volumns = set("aeiou")
		#조건1: 모음 하나를 반드시 포함해야함 - 하나라도 False(포함하지않으면) - False를 반환하는 not any
		if not any(ch in volumns for ch in word):
				return False
		#조건2: 모음이 3개 혹은 자음이 3개 오면 안됨
		count = 1
		if (word[i] in volums) == (word[i-1] in volums):
			count += 1
			if(count >= 3):
				return False 
			else:
				count = 1
		#조건3: 같은 글자가 연속적으로 두번 오면 안되나 , ee 와 oo는 허용 
		for i in range (1, len(word)):
			if word[i] == word[i-1]:
				if word[i] not in ['e','o']: #not in : 하나라도 연속적으로 두번이 오면 False이니, False를 반환하는 not in
					return False
		return True
#출력 함수 
def solution(word:list):
		for lst in word:
			if checkpwd(lst):
				print(f"<{lst}> is acceptable.")
			else:
			    print(f"<{lst}> is not acceptable.")
#입력
word = []
while True:
	lst = sys.stdin.readline().strip()
	if lst == "end":
		break
	word.append(lst)
solution(word)
