import sys
import re
input = sys.stdin.readline

t1 = input() #int& a*[]&, b, c*; 
#rstrip 
t1 = t1.strip().rstrip(';') #세미클론 삭제

casting = t1.split()
base_type = casting[0]
rest = ' '.join(casting[1:])

variables = [v.strip() for v in rest.split(',')] #, 기준으로 
for i in variables: # a*[]&
    ch = i[0]
    alpha = i[1::]
    variable =  re.findall(r'\*\*|\*|\[\]|\&|\w+', alpha)
    va = ''.join(variable[::-1])
    result = base_type + va + ' ' + ch
    print(result + ';')

